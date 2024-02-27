class Cliente:
    def __init__(self, nome, senha, cpf, idade):
        self.nome = nome
        self.senha = senha
        self.cpf = cpf
        self.idade = idade
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def depositar(self, indice_conta, valor):
        if 0 <= indice_conta < len(self.contas):
            self.contas[indice_conta].depositar(valor)
        else:
            print("Conta não encontrada.")

    def sacar(self, indice_conta, valor):
        if 0 <= indice_conta < len(self.contas):
            self.contas[indice_conta].sacar(valor)
        else:
            print("Conta não encontrada.")

    def exibir_extrato(self, indice_conta):
        if 0 <= indice_conta < len(self.contas):
            self.contas[indice_conta].exibir_extrato()
        else:
            print("Conta não encontrada.")

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
        print(f"\nDepósito de R${valor:.2f} efetuado com sucesso!")

    def sacar(self, valor):
        if valor <= 0 or valor > self.saldo:
            print("Valor inválido para saque!")
            return
        self.saldo -= valor
        print(f"\nSaque de R${valor:.2f} efetuado com sucesso!")

    def exibir_extrato(self):
        print("\n------------------Extrato------------------")
        print(f"Número da conta: {self.numero_conta}")
        print(f"Agência: {self.agencia}")
        print(f"Tipo da conta: {self.tipo_conta}")
        print(f"Saldo: R${self.saldo:.2f}")


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
        nome = input("Nome: ")
        senha = input("Senha: ")
        cpf = input("CPF: ")
        idade = int(input("Idade: "))
        cliente = Cliente(nome, senha, cpf, idade)
        clientes.append(cliente)
        print("\nCliente cadastrado com sucesso!")

    elif opcao == "2":
        if not clientes:
            print("\nÉ necessário cadastrar um cliente primeiro!")
            continue
        cliente_index = int(input("Índice do cliente: "))
        if 0 <= cliente_index < len(clientes):
            numero_conta = int(input("Número da conta: "))
            agencia = int(input("Agência: "))
            tipo_conta = input("Tipo da conta: ")
            conta = ContaBancaria(numero_conta, agencia, tipo_conta)
            clientes[cliente_index].adicionar_conta(conta)
            print("\nConta cadastrada com sucesso!")
        else:
            print("\nÍndice de cliente inválido!")

    elif opcao == "3":
        if not clientes:
            print("\nÉ necessário cadastrar um cliente primeiro!")
            continue
        cliente_index = int(input("Índice do cliente: "))
        if 0 <= cliente_index < len(clientes):
            conta_index = int(input("Índice da conta: "))
            valor = float(input("Valor do depósito: "))
            clientes[cliente_index].depositar(conta_index, valor)
        else:
            print("\nÍndice de cliente inválido!")

    elif opcao == "4":
        if not clientes:
            print("\nÉ necessário cadastrar um cliente primeiro!")
            continue
        cliente_index = int(input("Índice do cliente: "))
        if 0 <= cliente_index < len(clientes):
            conta_index = int(input("Índice da conta: "))
            valor = float(input("Valor do saque: "))
            clientes[cliente_index].sacar(conta_index, valor)
        else:
            print("\nÍndice de cliente inválido!")

    elif opcao == "5":
        if not clientes:
            print("\nÉ necessário cadastrar um cliente primeiro!")
            continue
        cliente_index = int(input("Índice do cliente: "))
        if 0 <= cliente_index < len(clientes):
            conta_index = int(input("Índice da conta: "))
            clientes[cliente_index].exibir_extrato(conta_index)
        else:
            print("\nÍndice de cliente inválido!")

    elif opcao == "6":
        print("\nSaindo...")
        break

    else:
        print("\nOpção inválida!")
