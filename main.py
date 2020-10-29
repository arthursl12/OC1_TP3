import argparse

"""
Entrada: um arquivo .txt, obtido dos argumentos, com as instruções
Saída: outro arquivo .txt, com os resultados das instruções
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
        help="(Opcional) Nome arquivo entrada",
        default="out.txt"
    )
    args = parser.parse_args()
    
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
            # TODO
            if (op == 1):
                result = "W"
            elif (op == 0):
                result = "M"
                qtd_misses += 1
            
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