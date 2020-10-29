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

if __name__ == "__main__":
    main()