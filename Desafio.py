menu = """

[d] Depositar
[s] Sacar 
[e] Extrato 
[q] Sair 

=> """

saldo = 0
limite = 500 
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3 

while True: 
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor <= 0:
            print("Valor inválido! Opercação falhou.")
        
        else:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
    
    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar: "))

        if valor <= 0:
            print("Valor inválido! Opercação falhou.")

        elif valor > saldo:
            print("Operação falhou! Valor maior que o seu saldo.")
        
        elif valor > limite:
            print("Operação falhou! Valor maior que seu limite")

        elif numero_saques >= LIMITES_SAQUES:
            print("Seu limite de saques já foi atingido; não é possível fazer a operação!")

        else: 
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1

    elif opcao == "e":
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida; por favor tente novamente!")