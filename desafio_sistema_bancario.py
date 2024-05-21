menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[9] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso.")

        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "2":
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Informe o valor que deseja sacar: "))
            if valor <= limite:
                if valor <= saldo:
                    saldo -= valor
                    numero_saques += 1
                    extrato += f"Saque: R$ {valor:.2f}\n"
                    print("Retire o dinheiro no local indicado")
                else:
                    print("Saldo insuficiente")
            else:
                print("Valor superior ao limite de saque.")
        else:
            print("Limite de saques excedido.")
    
    elif opcao == "3":
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")
       
    elif opcao == "9":
        break

    else:
        print("Opção inválida.")


        
        


