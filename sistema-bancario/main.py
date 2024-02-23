saldo:float = 0
extrato = []

def depositar(valor):
    global saldo
    if valor <= 0:
        print("Valor inválido para depósito!")
        return
    
    saldo += valor
    extrato.append(("Depósito", valor))
    print("");
    print("------------------Deposito------------------")
    print("Depósito de R$%.2f efetuado com sucesso!" % valor)
    
def sacar(valor):
    global saldo
    if valor <= 0 or valor > saldo:
        print("Valor inválido para saque!")
        return
    
    saldo -= valor
    extrato.append(("Saque", valor))
    
    print("");
    print("------------------Saque------------------")
    print("Saque de R$%.2f efetuado com sucesso!" % valor)
    
def exibirExtrato():
    if len(extrato) == 0:
        print("Nenhuma operação realizada!")
        return

    print("")
    print("------------------Extrato------------------")
    print("Extrato: ")
    for op in extrato:
        print(op[0], "de R$%.2f" % op[1])
    print("Saldo: R$%.2f" % saldo)

programa = 0

while programa != 4:
    print("")
    print("               Banco Python              ")
    print("-----------------------------------------")
    print("Escolha uma opção: ")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Sair")
    print("-----------------------------------------")
    programa = int(input("Opção: "))
    
    if programa == 1:
        valor = float(input("Digite o valor do depósito: "))
        depositar(valor)
    elif programa == 2:
        valor = float(input("Digite o valor do saque: "))
        sacar(valor)
    elif programa == 3:
        exibirExtrato()
    elif programa == 4:
        print("Saindo...")
    else:
        print("Opção inválida!")
