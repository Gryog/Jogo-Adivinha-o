def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


    palavra_secreta = "peixe".upper()
    letras_acertadas = ["_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(True):

        chute_str = input("Qual a Letra?")
        chute = chute_str.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Errou! Voce tem {} tentativas".format(6 - erros))

        if("_" not in letras_acertadas):
            break
        if(erros == 6):
            break
        print(letras_acertadas)

    if("_" not in letras_acertadas):
        print("Voce acertou!")
    else:
        print("Voce Perdeu!")
    print("Fim de Jogo")

if (__name__ == "__main__"):
    jogar()
