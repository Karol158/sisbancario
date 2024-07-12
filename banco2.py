import os
from datetime import date,datetime
nome = []
cpf =[]
numeroconta =[]
saldo =[]
historico=[]

data= date.today()
print(data)
hora = datetime.now()
print("Hora atual:", hora.strftime("%H:%M:%S"))
def limpar():
    os.system("cls")   
def criarconta():
    limpar()
    nome.append(input("seu nome:"))
    cpf.append(input("seu cpf:"))
    saldo.append(0)
    numeroconta.append(input("o numero da conta:"))
    limpar()
    menu() 
        
def alterar():
    limpar()
    print("Digite o numero da conta que você quer alterar")
    print("alterarcpf:'1'\n alterarnome:'2'")
    conta = input("Digite o numero da conta:")
    encontrado = False
    
    for i in range(len(numeroconta)):
        if numeroconta[i] == conta:
            print(f'Conta: {numeroconta[i]}\nCPF: {cpf[i]}\nNome: {nome[i]}\nSaldo: {saldo[i]}')
            encontrado = True
            break
    
    if not encontrado:
        limpar()
        menu()
    
    if conta == numeroconta[i]:
        pedido=input("O que voce deseja alterar")
    if pedido == '1':
        cpf[i] = input("Digite seu cpf novo:") 
    elif pedido == '2': 
        nome[i] = input("Digite seu novo nome:") 
        print()
    inicio = input("Digite 'sair' para voltar para o início: ")
    if inicio == 'sair':
        limpar()
        menu()  

def consultar():
    limpar()
    conta = input("O número da sua conta: ")
    encontrado = False
    for i in range(len(numeroconta)):
        if numeroconta[i] == conta:
            print(f'Conta: {numeroconta[i]}\nCPF: {cpf[i]}\nNome: {nome[i]}\nSaldo: {saldo[i]}')
            encontrado = True
            break
    if not encontrado:
        limpar()
        menu()
    
       
    voltar =input("Digite 'sair' pra voltar pro inicio")
    if voltar=='sair':
     limpar()
     menu() 

def excluirconta():
    limpar()
    print("Digite o numero da conta para exclui-lá")
    conta=input("digite o numero da conta:")
    encontrado = False
    for i in range(len(numeroconta)):
         if numeroconta[i] == conta:
            print(f'Conta: {numeroconta[i]}\nCPF: {cpf[i]}\nNome: {nome[i]}\nSaldo: {saldo[i]}')
            encontrado = True
            break
    
    if not encontrado:
          limpar()
          menu()
    
    
    if conta==numeroconta[i]:
          pedido=input("Voce quer excluir conta?")
    if pedido=="sim":     
          del(cpf[i])
          del(nome[i])
          del(numeroconta[i])
          del(saldo[i])
          print("conta excluída")
          print()
    inicio = input("Digite 'sair' para voltar para o início: ")
    if inicio == 'sair':
        limpar()
        menu()  
def depositar():
    limpar()
    valor=int(input("digite o valor a ser depositado:"))
    conta=input("Digite o numero da conta:")
    encontrado = False
    for i in range(len(numeroconta)):
         if numeroconta[i] == conta:
            print(f'Conta: {numeroconta[i]}\nCPF: {cpf[i]}\nNome: {nome[i]}\nSaldo: {saldo[i]}')
            encontrado = True
            break
    
    if not encontrado:
           limpar()
           menu()
    
    
    if conta == numeroconta[i]:
         saldo[i]=saldo[i]+valor
         historico.append(f'Você recebeu um valor de: {valor},hora:{hora.strftime("%H:%M:%S")} ')
         print("Valor depositado com sucesso.")
         print()
    inicio = input("Digite 'sair' para voltar para o início: ")
    if inicio == 'sair':
        limpar()
        menu()
def pix():
     limpar()
     valor=int(input("Qual o valor a transferir?"))
     conta=input("Digite o numero da sua conta")
     conta1=input("Digite o numero da conta que voce quer transferir:")
     indice = numeroconta.index(conta1)
     encontrado = False
     for i in range(len(numeroconta)):
         if numeroconta[i] == conta:
            print(f'Conta: {numeroconta[i]}\nCPF: {cpf[i]}\nNome: {nome[i]}\nSaldo: {saldo[i]}')
            encontrado = True
            break
    
     if not encontrado:
           limpar()
           menu()
    
     if conta == numeroconta[i]:
         saldo[i]=saldo[i]-valor
         saldo[indice]=saldo[indice]+valor
         
     historico.append(f'Você fez um pix de:{valor},no dia:{data},hora:{hora.strftime("%H:%M:%S")} ')
     print("Pix realizado")
     print()
     saida = input("Digite 'sair' para voltar para o início: ")
     if saida == 'sair':
        limpar()
        menu()

def histórico():
    limpar()
    print("Digite o numero da conta para ver o seu historico")
    conta=input("Digite o numero da conta")
    for i in range(len(numeroconta)):
         if numeroconta[i] == conta:
             print(historico)
         else:
             print("Essa conta não existe")
             print()
    saida = input("Digite 'sair' para voltar para o início: ")
    if saida == 'sair':
           limpar()
           menu()
    
#isso é um comentario
def menu():
    print("Sistema Bancário")
    print("\n \n '1'criar conta\n '2'alterar conta \n '3'consultar conta\n '4'excluir conta \n '5'depositar\n '6'fazer pix\n '7'Ver meus histórico")
    x = input("o que voce quer fazer?")
    
    if x == '1':
      limpar()
      criarconta()

    elif x == '3':
     limpar()
     consultar()
     
    elif x =='2':
       limpar()
       alterar()

    elif x=='4':
       limpar()
       excluirconta()
    elif x=='5':
        limpar()
        depositar()

    elif x=='6':
        limpar()
        pix()
    elif x=='7':
        limpar()
        histórico()
    else:
         limpar()
         print("Ops!,ocorreu um erro,tente novamente.")
         menu()
        
limpar()
menu() 