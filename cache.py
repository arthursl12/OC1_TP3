class Cache:
    """
    Classe Cache: possui 64 blocos de 4 palavras. Busca se uma palavra está na cache
    ou não, retorna Hit ou Miss, além do dado. Em caso de Miss, o bloco do dado é 
    carregado da memória principal. Para escrita, é feita uma busca inicialmente, 
    as alterações são feitas em princípio apenas na cache e quando esse bloco sair,
    se ele estiver marcado como "sujo" a memória deverá sobrescrevê-lo
    """
    pass