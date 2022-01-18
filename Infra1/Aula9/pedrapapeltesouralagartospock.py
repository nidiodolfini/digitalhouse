#encoding:UTF-8
import random
import sys

def get_int():
    userdata = input("Digite um número, ou 's' para sair do programa ")
    if userdata == 's':
        print ("Nos vemos!")
        sys.exit()
    try:
        user_num = int(userdata)
        return user_num
    except ValueError:
        print("Precisa de um número para continuar: ")
        return(get_int())

while True: 
    aleatorio = random.randrange(0, 5)
    escolhaPc = ""
    again = ""
    print("1)Pedra")
    print("2)Papel")
    print("3)Tesoura")
    print("4)Lagarto")
    print("5)Spock")
    opcao = get_int()
    
    if opcao == 1:
        escolhaUsuario = "pedra"
    elif opcao == 2:
        escolhaUsuario = "papel"
    elif opcao == 3:
        escolhaUsuario = "tesoura"
    elif opcao == 4:
        escolhaUsuario = "lagarto"
    elif opcao == 5:
        escolhaUsuario = "spock"
    else:
        print("Opção Invalida")
        continue
        
    print("Você escolheu: ", escolhaUsuario)    
    if aleatorio == 0:
        escolhaPc = "pedra"
    elif aleatorio == 1:
        escolhaPc = "papel"
    elif aleatorio == 2:
        escolhaPc = "tesoura"
    elif aleatorio == 3:
        escolhaPc = "lagarto"
    elif aleatorio == 4:
        escolhaPc = "spock"
    print("PC escolheu: ", escolhaPc)
    print("...")
    
    if escolhaPc == "pedra" and escolhaUsuario == "papel":
        print("Ganhou, papel cobre pedra")
    elif escolhaPc == "papel" and escolhaUsuario == "tesoura":
        print("Ganhou, tesoura corta papel")
    elif escolhaPc == "tesoura" and escolhaUsuario == "pedra":
        print("Ganhou, pedra amassa tesoura")
    elif escolhaPc == "lagarto" and escolhaUsuario == "pedra":
        print("Ganhou, pedra esmaga a lagarto")
    elif escolhaPc == "lagarto" and escolhaUsuario == "tesoura":
        print("Ganhou, tesoura decapita a Lagarto")
    elif escolhaPc == "tesoura" and escolhaUsuario == "spock":
        print("Ganhou, Spock quebra tesoura")
    elif escolhaPc == "spock" and escolhaUsuario == "lagarto":
        print("Ganhou, lagarto envenena a Spock")
    elif escolhaPc == "papel" and escolhaUsuario == "lagarto":
        print ("Ganhou, lagarto come papel")
    elif escolhaPc == "spock" and escolhaUsuario == "papel":
        print ("Ganhou, papel refuta a Spock")
    elif escolhaPc == "pedra" and escolhaUsuario == "spock":
        print ("Ganhou, Spock vaporiza pedra")
        
    if escolhaUsuario == "pedra" and escolhaPc == "papel":
        print("Perdeu, papel cobre pedra")
    elif escolhaUsuario == "papel" and escolhaPc == "tesoura":
        print("Perdeu, tesoura corta papel")
    elif escolhaUsuario == "tesoura" and escolhaPc == "pedra":
        print("Perdeu, pedra amassa tesoura")
    elif escolhaUsuario == "lagarto" and escolhaPc == "pedra":
        print("Perdeu, pedra esmaga a lagarto")
    elif escolhaUsuario == "lagarto" and escolhaPc == "tesoura":
        print("Perdeu, tesoura decapita a Lagarto")
    elif escolhaUsuario == "tesoura" and escolhaPc == "spock":
        print("Perdeu, Spock quebra tesoura")
    elif escolhaUsuario == "spock" and escolhaPc == "lagarto":
        print("Perdeu, lagarto envenena a Spock")
    elif escolhaUsuario == "papel" and escolhaPc == "lagarto":
        print ("Perdeu, lagarto come papel")
    elif escolhaUsuario == "spock" and escolhaPc == "papel":
        print ("Perdeu, papel refuta a Spock")
    elif escolhaUsuario == "pedra" and escolhaPc == "spock":
        print ("Perdeu, Spock vaporiza pedra")
    elif escolhaPc == escolhaUsuario:
        print("Empate")
    while again == "":
        again = input("Vamos jogar de novo? s/n: ")
        if 's' in again:
            break
        elif 'n' in again:
            print("Nos vemos!")
            sys.exit()
        else:
            print("Valor Invalido")
            again = ""
            continue 