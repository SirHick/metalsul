class Funcionario:
    def __init__(self, id, nome, cargo, salario, setor):
        self.__id = id
        self.__nome = nome
        self.__cargo = cargo
        self.__salario = salario
        self.__setor = setor

    def trocar_cargo(self, novo_cargo):
        self.__cargo = novo_cargo

    def aumentar_salario(self, valor):
        if valor < 0:
            raise ValueError(
                f"O aumento {valor} precisa ser maior ou igual a zero."
            )
        self.__salario += valor

    def mostrar_dados(self):
        print("*" * 25)
        print(f"ID: {self.__id}")
        print(f"NOME: {self.__nome}")
        print(f"CARGO: {self.__cargo}")
        print(f"SALÁRIO: {self.__salario}")
        print(f"SETOR: {self.__setor.nome}")
        print("*" * 25)

    @property
    def setor(self):
        return self.__setor

    # Getters
    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def cargo(self):
        return self.__cargo

    @property
    def salario(self):
        return self.__salario

    # Setters
    @nome.setter
    def nome(self, novo_nome):
        if novo_nome == '':
            raise ValueError(
                "O novo nome não pode estar vazio/em branco. Inválido."
            )
        self.__nome = novo_nome

    @cargo.setter
    def cargo(self, novo_cargo):
        if novo_cargo == '':
            raise ValueError(
                "O novo cargo não pode ser vazio/estar em branco. Inválido."
            )
        self.__cargo = novo_cargo

    @salario.setter
    def salario(self, novo_salario):
        if novo_salario <= 0:
            raise ValueError(
                "O salário precisa ser maior que zero. Inválido."
            )
        self.__salario = novo_salario