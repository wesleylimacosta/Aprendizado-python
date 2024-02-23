class Cliente:
    def __init__(self, nome, senha, cpf, idade):
        self.nome = nome
        self.senha = senha
        self.cpf = cpf
        self.idade = idade
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class ContaBancaria:
    def __init__(self, numero_conta, agencia, tipo_conta="corrente"):
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.tipo_conta = tipo_conta
        self.saldo = 0

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido para depósito!")
            return
        self.saldo += valor

    def sacar(self, valor):
        if valor <= 0 or valor > self.saldo:
            print("Valor inválido para saque!")
            return
        self.saldo -= valor

    def exibir_extrato(self):
        print("\n------------------Extrato------------------")
        print(f"Número da conta: {self.numero_conta}")
        print(f"Agência: {self.agencia}")
        print(f"Tipo da conta: {self.tipo_conta}")
        print(f"Saldo: R${self.saldo:.2f}")


def cadastrar_cliente():
    nome = input("Nome: ")
    senha = input("Senha: ")
    cpf = input("CPF: ")
    idade = int(input("Idade: "))
    return Cliente(nome, senha, cpf, idade)


def cadastrar_conta(cliente):
    numero_conta = int(input("Número da conta: "))
    agencia = int(input("Agência: "))
    tipo_conta = input("Tipo da conta: ")
    conta = ContaBancaria(numero_conta, agencia, tipo_conta)
    cliente.adicionar_conta(conta)
    print("\nConta cadastrada com sucesso!")


def depositar(conta):
    valor = float(input("Valor do depósito: "))
    conta.depositar(valor)
    print(f"\nDepósito de R${valor:.2f} efetuado com sucesso!")


def sacar(conta):
    valor = float(input("Valor do saque: "))
    conta.sacar(valor)
    print(f"\nSaque de R${valor:.2f} efetuado com sucesso!")


def exibir_extrato(conta):
    conta.exibir_extrato()


clientes = []

while True:
    print("\n               Banco Python              ")
    print("-----------------------------------------")
    print("Escolha uma opção: ")
    print("1 - Cadastrar cliente")
    print("2 - Cadastrar conta bancária")
    print("3 - Depositar")
    print("4 - Sacar")
    print("5 - Extrato")
    print("6 - Sair")
    print("-----------------------------------------")

    opcao = input("Opção: ")

    if opcao == "1":
        cliente = cadastrar_cliente()
        clientes.append(cliente)
        print("\nCliente cadastrado com sucesso!")

    elif opcao == "2":
        if not clientes:
            print("\nÉ necessário cadastrar um cliente primeiro!")
            continue
        cliente_index = int(input("Índice do cliente: "))
        if cliente_index < 0 or cliente_index >= len(clientes):
            print("\nÍndice de cliente inválido!")
            continue
        cadastrar_conta(clientes[cliente_index])

    elif opcao == "3":
        if not clientes:
            print("\nÉ necessário cadastrar um cliente primeiro!")
            continue
        cliente_index = int(input("Índice do cliente: "))
        if cliente_index < 0 or cliente_index >= len(clientes):
            print("\nÍndice de cliente inválido!")
            continue
        conta_index = int(input("Índice da conta: "))
        if conta_index < 0 or conta_index >= len(clientes[cliente_index].contas):
            print("\nÍndice de conta inválido!")
            continue
        depositar(clientes[cliente_index].contas[conta_index])

    elif opcao == "4":
        if not clientes:
            print("\nÉ necessário cadastrar um cliente primeiro!")
            continue
        cliente_index = int(input("Índice do cliente: "))
        if cliente_index < 0 or cliente_index >= len(clientes):
            print("\nÍndice de cliente inválido!")
            continue
        conta_index = int(input("Índice da conta: "))
        if conta_index < 0 or conta_index >= len(clientes[cliente_index].contas):
            print("\nÍndice de conta inválido!")
            continue
        sacar(clientes[cliente_index].contas[conta_index])

    elif opcao == "5":
        if not clientes:
            print("\nÉ necessário cadastrar um cliente primeiro!")
            continue
        cliente_index = int(input("Índice do cliente: "))
        if cliente_index < 0 or cliente_index >= len(clientes):
            print("\nÍndice de cliente inválido!")
            continue
        conta_index = int(input("Índice da conta: "))
        if conta_index < 0 or conta_index >= len(clientes[cliente_index].contas):
            print("\nÍndice de conta inválido!")
            continue
        exibir_extrato(clientes[cliente_index].contas[conta_index])

    elif opcao == "6":
        print("\nSaindo...")
        break

    else:
        print("\nOpção inválida!")
