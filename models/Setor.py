class Setor:
    def __init__(self, id, nome):
        self.__id = id
        self.__nome = nome


    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def apresentar(self):
        print("="*25)
        print(f"ID: {self.__id}")
        print(f"NOME DO SETOR: {self.__nome}")
        print("=" * 25)

    @nome.setter
    def nome(self, novo_nome):
        if novo_nome == '':
            raise ValueError ("Pô mano! Coloca um nome aí!")
        self.__nome = novo_nome