def jogar():
    print("*******************************")
    print("* Bem vindo ao jogo da Forca! *")
    print("*******************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip()

        posicao = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(chute, posicao))
            posicao = posicao + 1

        print("Jogando...")

    print("Fim do jogo!")


# Se o arquivo foi executado diretamente, roda o jogar (evita executar no import)
if (__name__ == "__main__"):
    jogar()
