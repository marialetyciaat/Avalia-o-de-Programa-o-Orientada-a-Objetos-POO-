class Banco:
    def __init__(self):
        # Agregação: o banco possui contas, mas elas podem ser independentes
        self.__contas = []

    def adicionar_conta(self, conta):
        self.__contas.append(conta)

    def buscar_conta(self, numero):
        for conta in self.__contas:
            if conta._numero == numero:
                return conta
        return None