class Cliente:
    def __init__(self, nome, cpf):
        # Atributos privados (Encapsulamento)
        self.__nome = nome
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome