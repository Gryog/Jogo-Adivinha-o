import random


def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0

    print("Qual Nivel de Dificuldade?")
    print("(1) Facil (2) Medio (3) Dificil")
    pontos = 1000

    nivel = int(input("Define o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        # interpolação de string
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        # Outra forma de formatar
        #print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute_str = input("Digite um numero entre 1 e 100: ")
        print("Voce digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Voce deve digitar um numero entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Voce Acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Voce Errou! O seu chute foi maior que o numero secreto")
            elif(menor):
                print("Voce Errou! O seu chute foi menor que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1
    print("Fim do Jogo")

if(__name__ == "__main__"):
    jogar()