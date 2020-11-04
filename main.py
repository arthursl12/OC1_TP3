import argparse

from cache import Cache, Query
from memoria import Memoria

"""
Entrada: um arquivo .txt, obtido dos argumentos, com as instruções
Saída: outro arquivo .txt, com os resultados das instruções, opcional 
(padrão=out.txt)
"""
def main():
    # Lê os argumentos para obter nome dos arquivos de entrada e saída
    parser = argparse.ArgumentParser()
    parser.add_argument("arq_entrada", help="Nome arquivo entrada")
    parser.add_argument(
        "-s",
        "--arquivo-saida",
        action="store",
        type=str,
        dest="arq_saida",
        help="(Opcional) Nome arquivo saída",
        default="out.txt"
    )
    args = parser.parse_args()
    
    # Inicialização do sistema
    cache = Cache()
    memoria = Memoria()
    
    # Leitura e Processamento
    qtd_misses = 0
    qtd_hits = 0
    qtd_reads = 0
    qtd_writes = 0
    linhas_lidas = []       #Para impressão na saída
    with open(args.arq_entrada, "r") as in_file:
        for line in in_file.readlines():
            # Tratamento da linha
            temp = ' '.join(line.split())   #Junta espaços múltiplos
            info = temp.split(' ')          #Separa por espaços
            
            # Extrai as informações
            endereco = int(info[0])
            op = int(info[1])
            assert ((op == 0) or (op == 1)) == True
            if (op == 1):
                dado = info[2]
                qtd_writes += 1
            elif (op == 0):
                qtd_reads += 1
                
            # Processamento
            if (op == 1):
                result = "W"
                hit_or_miss, palavra = cache.busca(endereco)
                bloco = cache.read_bloco(endereco)
                if (hit_or_miss == Query.MISS):
                    # Se o bloco estiver sujo, escreve o dado na memória
                    if bloco.get_sujo():
                        memoria.write_bloco(bloco)
                # Lê o bloco da memória para a cache
                cache.write_from_memory(endereco, memoria.get_bloco(endereco)) 
                # Escreve o dado no bloco da cache e marca como sujo.
                cache.write_from_input(endereco, dado)
            elif (op == 0):
                hit_or_miss, palavra = cache.busca(endereco)
                if (hit_or_miss == Query.MISS):
                    result = "M"
                    qtd_misses += 1
                    # Busca o bloco na cache
                    bloco = cache.read_bloco(endereco)
                    # Se o bloco estiver sujo, escreve o dado na memória
                    if bloco.get_sujo():
                        memoria.write_bloco(bloco)

                    # Lê da memória para a cache e marca o bit como não sujo.
                    cache.write_from_memory(endereco, memoria.get_bloco(endereco)) 
                else:
                    result = "H"
                    qtd_hits += 1
            
            # Armazenamento para impressão na saída
            line = line.strip()     #Remove o newline do final da linha
            linhas_lidas.append((line.strip(),result))
            
    # Saída     
    with open(args.arq_saida, "w") as out_file:
        out_file.write(f"READS: {qtd_reads}\n")
        out_file.write(f"WRITES: {qtd_writes}\n")
        out_file.write(f"HITS: {qtd_hits}\n")
        out_file.write(f"MISSES: {qtd_misses}\n")
        out_file.write(f"HIT RATE: {float(qtd_hits) / qtd_reads}\n")
        out_file.write(f"MISS RATE: {float(qtd_misses) / qtd_reads}\n")
        out_file.write("\n")
        for pair in linhas_lidas:
            out_file.write(f"{pair[0]} {pair[1]}\n")

if __name__ == "__main__":
    main()
