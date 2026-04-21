class Historico:
    def __init__(self):
        self.__transacoes = []

    def adicionar_transacao(self, texto):
        self.__transacoes.append(texto)

    def listar(self):
        return self.__transacoes