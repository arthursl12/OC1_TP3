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
    print(args.arq_entrada)
    print(args.arq_saida)
    
    # Leitura, processamento e escrita
    with open(args.arq_entrada, "r") as in_file:
        with open(args.arq_saida, "w") as out_file:
            for line in in_file.readlines():
                # Tratamento da linha
                temp = ' '.join(line.split())   #Junta espaços múltiplos
                info = temp.split(' ')          #Separa por espaços
                
                # Extrai as informações
                endereco = int(info[0])
                op = int(info[1])
                if (op == 1):
                    dado = info[2]
                
                # Processamento
                # TODO
                
                # Saída
                if (op == 1):
                    out_file.write(f"lido: {endereco}, {op}, {dado}\n")
                else:
                    out_file.write(f"lido: {endereco}, {op}\n")

if __name__ == "__main__":
    main()