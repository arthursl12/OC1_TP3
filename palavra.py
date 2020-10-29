class Palavra:
    """
    Classe Palavra: estrutura de dados para armazenar tanto o endereço da 
    palavra bem como o seu dado. O endereço é inteiro. O dado é uma string.
    """
    def __init__(self, endereco, dado):
        assert type(endereco) == int
        self.endereco = endereco
        
        assert type(dado) == str
        assert len(dado) <= 32
        self.dado = dado
    
    def get_indice(self):
        """Retorna o inteiro referente ao índice do endereço da palavra"""
        # Transforma o endereço inteiro em binário de 32bits, mantendo os zeros
        bin_end = '{0:032b}'.format(self.endereco)
        # Extrai o índice, após o offset
        indice_bin = bin_end[-8:-2]
        
        return int(indice_bin, 2)

    def get_offset(self):
        """Retorna o inteiro referente ao offset do endereço da palavra"""
        # Transforma o endereço inteiro em binário de 32bits, mantendo os zeros
        bin_end = '{0:032b}'.format(self.endereco)
        # Extrai o índice, após o offset
        offset_bin = bin_end[-2:]
        
        return int(offset_bin, 2)

    def get_tag(self):
        """Retorna o inteiro referente à tag do endereço da palavra"""
        # Transforma o endereço inteiro em binário de 32bits, mantendo os zeros
        bin_end = '{0:032b}'.format(self.endereco)
        # Extrai o índice, após o offset
        tag_bin = bin_end[:-8]
        
        return int(tag_bin, 2)

    def __eq__(self, outra_palavra):
        if (
            (self.endereco == outra_palavra.endereco) 
            and (self.dado == outra_palavra.dado)
            ):
            return True
        else:
            return False
        