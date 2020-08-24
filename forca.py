def jogar():
    print("*******************************")
    print("* Bem vindo ao jogo da Forca! *")
    print("*******************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        chute = input("Qual letra? ")

        posicao = 0
        for letra in palavra_secreta:
            if (chute == letra):
                print("Encontrei a letra {} na posição {}".format(chute, posicao))
            posicao = posicao + 1

        print("Jogando...")

    print("Fim do jogo!")


# Se o arquivo foi executado diretamente, roda o jogar (evita executar no import)
if (__name__ == "__main__"):
    jogar()
