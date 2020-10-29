from palavra import Palavra
class Bloco:
    """ 
    Classe Bloco: representa um bloco que possui 4 palavras de 32bits. Dentro 
    dele as palavras são indexadas de 0 a 3, sendo esse índice obtido dos dois 
    últimos bits do seu endereço ou do resto dividindo-o por 4 (via mod 4).
    """
    def __init__(self):
        self.palavras = []
        self.valido = False
        self.sujo = False
    
    def get_valido(self):
        return self.valido
    
    def get_sujo(self):
        return self.sujo
    
    def insert(self, p1, p2, p3, p4):
        """
        Insere as quatro palavras no bloco, desde que possuam o mesmo campo
        índice no endereço, seguindo o offset de cada um para armazenar
        """
        # Verifica se as palavras tem o mesmo campo índice
        palavras = [p1,p2,p3,p4]
        indice = p1.get_indice()
        for p in palavras:
            assert p.get_indice() == indice
        
        # Insere cada um na posição, com base no offset
        for p in palavras:
            offset = p.get_offset()
            self.palavras.insert(offset, p)
        assert len(self.palavras) == 4
        self.valido = True
    
    def get(self, offset):
        """Retorna a palavra com offset fornecido"""
        assert offset < 4
        assert offset >= 0
        return self.palavras[offset]
    
    def write(self, offset, new_dado):
        """Escreve o dado no endereço com offset fornecido"""
        old = self.palavras[offset]
        self.palavras[offset] = Palavra(old.endereco, new_dado)
        self.sujo = True
        
        # Verifica integridade: todas as palavras do bloco possuem o mesmo 
        # campo índice
        indice = self.palavras[0].get_indice()
        for p in self.palavras:
            assert p.get_indice() == indice
        