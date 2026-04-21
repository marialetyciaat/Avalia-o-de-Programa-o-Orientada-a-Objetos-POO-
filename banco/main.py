from clientes.cliente import Cliente
from contas.conta_corrente import ContaCorrente
from contas.conta_poupanca import ContaPoupanca
from sistema.banco import Banco

def iniciar():
    meu_banco = Banco()
    while True:
        print("\n=== CAIXA ELETRÔNICO ===")
        print("1- Criar Conta\n2- Depositar\n3- Sacar\n4- Saldo\n5- Histórico\n0- Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome: ")
            num = input("Número da conta: ")
            tipo = input("1-Corrente, 2-Poupança: ")
            cli = Cliente(nome, "000")
            nova = ContaCorrente(num, cli) if tipo == "1" else ContaPoupanca(num, cli)
            meu_banco.adicionar_conta(nova)
            print("Conta criada com sucesso!")

        elif opcao in ["2", "3", "4", "5"]:
            num = input("Número da conta: ")
            conta = meu_banco.buscar_conta(num)
            if conta:
                if opcao == "2":
                    val = float(input("Valor: "))
                    conta.depositar(val)
                elif opcao == "3":
                    val = float(input("Valor: "))
                    conta.sacar(val)
                elif opcao == "4":
                    print(f"Saldo: R$ {conta.saldo:.2f}")
                elif opcao == "5":
                    for op in conta._historico.listar():
                        print(op)
            else:
                print("Conta não encontrada!")
        elif opcao == "0":
            break

if __name__ == "__main__":
    iniciar()