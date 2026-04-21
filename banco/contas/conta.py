from operacoes.historico import Historico

class Conta:
    def __init__(self, numero, cliente):
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0.0
        # Composição: a conta cria seu próprio histórico
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._historico.adicionar_transacao(f"Depósito: R$ {valor:.2f}")
            return True
        return False

    def sacar(self, valor):
        # Método a ser definido nas subclasses (Polimorfismo)
        pass