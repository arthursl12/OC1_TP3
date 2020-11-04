from palavra import Palavra
from bloco import Bloco

class Memoria:
    """
    Classe Memória: possui 1024 palavras, inicialmente todas 0, endereçadas de 
    0 a 1023. É capaz de carregar um bloco a partir de um endereço de uma 
    palavra nele e também de, ao receber um bloco, verificar se este está sujo 
    e, se sim, sobrescrevê-lo 
    """

    def __init__(self):
        self.palavras = []
        for i in range(1024):
            self.palavras.insert(i, '0000000000000000000000000000000')

    def write_bloco(self, bloco):
        """ Escreve um bloco na memória a partir do endereço """
        assert type(endereco) == int
        # Transforma o endereço inteiro em binário de 32bits, mantendo os zeros
        bin_end = '{0:032b}'.format(endereco)
        # Extrai o tag, índice e offset
        tag = int(bin_end[:-8], 2)
        indice = int(bin_end[-8:-2], 2)
        offset = int(bin_end[-2:], 2)

        self.palavras[bloco.get(0).endereco] = bloco.get(0).dado
        self.palavras[bloco.get(1).endereco] = bloco.get(1).dado
        self.palavras[bloco.get(2).endereco] = bloco.get(2).dado
        self.palavras[bloco.get(3).endereco] = bloco.get(3).dado


    def get_bloco(self, endereco):
        """Retorna o bloco que contém o endereço"""
        assert type(endereco) == int
        # Transforma o endereço inteiro em binário de 32bits, mantendo os zeros
        bin_end = '{0:032b}'.format(endereco)
        # Extrai o tag, índice e offset
        tag = int(bin_end[:-8], 2)
        indice = int(bin_end[-8:-2], 2)
        offset = int(bin_end[-2:], 2)

        if offset == 0:
            bloco = Bloco()
            bloco.insert(
                    Palavra(endereco, self.palavras[endereco]),
                    Palavra(endereco+1, self.palavras[endereco+1]),
                    Palavra(endereco+2, self.palavras[endereco+2]),
                    Palavra(endereco+3, self.palavras[endereco+3])
                    )
        elif offset == 1:
            bloco = Bloco()
            bloco.insert(
                    Palavra(endereco-1, self.palavras[endereco-1]),
                    Palavra(endereco, self.palavras[endereco]),
                    Palavra(endereco+1, self.palavras[endereco+1]),
                    Palavra(endereco+2, self.palavras[endereco+2])
                    )
        elif offset == 2:
            bloco = Bloco()
            bloco.insert(
                    Palavra(endereco-2, self.palavras[endereco-2]),
                    Palavra(endereco-1, self.palavras[endereco-1]),
                    Palavra(endereco, self.palavras[endereco]),
                    Palavra(endereco+1, self.palavras[endereco+1])
                    )
        else:
            bloco = Bloco()
            bloco.insert(
                    Palavra(endereco-3, self.palavras[endereco-3]),
                    Palavra(endereco-2, self.palavras[endereco-2]),
                    Palavra(endereco-1, self.palavras[endereco-1]),
                    Palavra(endereco, self.palavras[endereco])
                    )
        return bloco
