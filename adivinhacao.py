print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas > 0):
    print("Tentativa {} de {}".format(rodada,total_de_tentativas))#interpolação de string
    ##Outra forma de formatar
    #print(f"Tentativa {rodada} de {total_de_tentativas}")
    chute_str = input("Digite o seu numero: ")
    print("Voce digitou ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Voce Acertou!")
    else:
        if(maior):
            print("Voce Errou! O seu chute foi maior que o numero secreto")
        elif(menor):
            print("Voce Errou! O seu chute foi menor que o numero secreto")

    rodada = rodada + 1
print("Fim do Jogo")
