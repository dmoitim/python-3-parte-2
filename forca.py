import random


def jogar():
    print("*******************************")
    print("* Bem vindo ao jogo da Forca! *")
    print("*******************************")

    palavras = []

    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    arquivo.close()

    indice = random.randrange(0, len(palavras))
    palavra_secreta = palavras[indice].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    tentativas = 0

    print(letras_acertadas)
    letras_faltando = str(letras_acertadas.count("_"))

    while (not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[posicao] = letra
                    letras_faltando = int(letras_acertadas.count("_"))
                posicao += 1
        else:
            tentativas += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6-tentativas))

        enforcou = tentativas == 6
        acertou = letras_faltando == 0

        print(letras_acertadas)
        print("Ainda falta acertar {} letras.".format(letras_faltando))

    if (acertou):
        print("Você ganhou!!!")
    else:
        print("Você perdeu.")

    print("Fim do jogo!")


# Se o arquivo foi executado diretamente, roda o jogar (evita executar no import)
if (__name__ == "__main__"):
    jogar()
