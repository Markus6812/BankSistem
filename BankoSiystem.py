Menu = """
[d] Depositar
[s] Sacar
[e] extrato
[q] sair

"""

saldo = 0
limite = 600
extrato = "" 
numero_saques = 0
limite_saques = 3

while True:
    opção = input(Menu)
    
    if opção == "d":
        valor = float(input("informe o valor do depósito"))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("Valor inválido, deposito não realizado")
            
    elif opção == "s":
        valor = float(input("informe o valor do Saque"))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques > limite_saques
        
        if excedeu_saldo:
            print("Saldo insuficiente")
            
        elif excedeu_limite:
            print("Excedeu limite de saque")
            
        elif excedeu_saques:
            print("Limite de saques ulrapassado")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            
        else:
            print("Operação não realizada, valor inválido")   
            
    elif opção == "e":
        print("\n===============EXTRATO===============")
        print("Sem Operacões no período." if not extrato else extrato )
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        
    elif opção == "q":
        break
    else:
        print("Operação inválida, tente novamente")          
            
                        