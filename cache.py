from enum import Enum

from bloco import Bloco

class Query(Enum):
    """Simbolizar um cache hit e um cache miss"""
    MISS = 0
    HIT = 1
    
class Cache:
    """
    Classe Cache: possui 64 blocos de 4 palavras. Busca se uma palavra está na 
    cache ou não, retorna Hit ou Miss, além do dado. Em caso de Miss, o bloco do
    dado é carregado da memória principal. Para escrita, é feita uma busca 
    inicialmente, as alterações são feitas em princípio apenas na cache e quando
    esse bloco sair, se ele estiver marcado como "sujo" a memória deverá 
    sobrescrevê-lo.
    
    É inicializada com blocos vazios em todas as 64 posições.
    """
    def __init__(self):
        self.blocos = []
        for i in range(64):
            self.blocos.insert(i, Bloco())
    
    def busca(self, endereco):
        assert type(endereco) == int
        # Transforma o endereço inteiro em binário de 32bits, mantendo os zeros
        bin_end = '{0:032b}'.format(endereco)
        # Extrai o tag, índice e offset
        tag = int(bin_end[:-8], 2)
        indice = int(bin_end[-8:-2], 2)
        offset = int(bin_end[-2:], 2)
        
        result = self.blocos[indice].get(offset)
        if (result is None):
            return Query.MISS, None
        else:
            assert result.get_tag() == tag
            return Query.HIT, result
