class Comando:
    def __init__(self, comando, saida, ativo, script, id_comando=None):
        self.__comando = comando
        self.__saida = saida
        self.__ativo = ativo
        self.__script = script
        self.__id_comando = id_comando

    @property
    def comando(self):
        return self.__comando

    @property
    def saida(self):
        return self.__saida

    @property
    def ativo(self):
        return self.__ativo
        
    @property
    def script(self):
        return self.__script
    
    @property
    def id_comando(self):
        return self.__id_comando
    
    @id_comando.setter
    def id_comando(self, id):
        self.__id_comando = id
