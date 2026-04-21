from contas.conta import Conta

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            self._historico.adicionar_transacao(f"Saque CP: R$ {valor:.2f}")
            return True
        print("Saldo insuficiente na Poupança!")
        return False