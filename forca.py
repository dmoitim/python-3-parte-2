def jogar():
    print("*******************************")
    print("* Bem vindo ao jogo da Forca! *")
    print("*******************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while (not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip()

        posicao = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[posicao] = letra
                letras_faltando = str(letras_acertadas.count("_"))
            posicao = posicao + 1

        print(letras_acertadas)
        print("Ainda falta acertar {} letras.".format(letras_faltando))

    print("Fim do jogo!")


# Se o arquivo foi executado diretamente, roda o jogar (evita executar no import)
if (__name__ == "__main__"):
    jogar()
