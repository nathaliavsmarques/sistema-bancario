print('-*' * 15)
print('Sistema Eletrônico Financeiro')
print('-*' * 15)
print('''    O que deseja fazer ?
      
    Consultar Saldo: [A]
    Depositar: [B]
    Sacar: [C]
    Transferir Valor: [D]
    Sair: [E]''')

print('-' * 30)

saldo = 0      

while True:
    opcao = input('Digite Opção: ').upper()
    if opcao =='A':
        print(f'Seu saldo é de R$ {saldo:.2f}')        
    elif opcao =='B':
        deposito = float(input('Informe o valor do depósito: R$  '))
        saldo += deposito
        print(f'Você depositou R$ {deposito:.2f}.')
        print(f'Seu saldo agora é de: R$ {saldo:.2f}')        
    elif opcao =='C':
        saque = float(input('Informe o valor do saque: R$ '))
        if saque > saldo :
            print(f'Erro na operação, você não possui saldo suficiente.\nSeu saldo é de R$ {saldo:.2f}')
        else: 
            saldo -= saque
            print(f'Você sacou R$ {saque:.2f}. \nSeu saldo agora é de: R$ {saldo:.2f}')
        print(f'')        
    elif opcao =='D':
        cpf = input('Informe o CPF do destinatário: ')
        tratando_cpf = cpf.replace('.', '').replace('-', '')
        if len(tratando_cpf) != 11:
            print('O CPF deve conter 11 dígitos numéricos.')
        else:
            transferir = float(input('Informe o valor que deseja transferir: R$ '))
            if saldo < transferir:
                print('Erro, saldo insuficiente.')
            else: 
                saldo -= transferir
                print(f'Você transferiu R$ {transferir:.2f} para o CPF {cpf}.\nSeu saldo agora é de R$ {saldo:.2f}')        
    elif opcao =='E':
        print('Você escolheu letra E')
    else:
        print('Você escolheu uma opção inválida')    
    
    continuar = input('Deseja fazer outra operação ?: [S/N] ').upper()
    if continuar == 'N':
        print('-*' * 10)
        print('OPERAÇÃO ENCERRADA')
        print('-*' * 10)       
        break   