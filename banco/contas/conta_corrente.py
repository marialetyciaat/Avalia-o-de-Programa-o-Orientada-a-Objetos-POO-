from contas.conta import Conta

class ContaCorrente(Conta):
    def sacar(self, valor):
        # Regra de Negócio: Não permite saque com saldo insuficiente [cite: 57]
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            self._historico.adicionar_transacao(f"Saque CC: R$ {valor:.2f}")
            return True
        print("Saldo insuficiente na Corrente!")
        return False