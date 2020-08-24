import forca
import adivinhacao


def escolher_jogo():
    print("*************************************")
    print("******** Escolha o seu jogo! ********")
    print("*************************************")

    print("(1) Forca   (2) Adivinhação")
    jogo = int(input("Qual jogo? "))

    if (jogo == 1):
        print("Jogando da forca.")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando de adivinhação.")
        adivinhacao.jogar()


# Se o arquivo foi executado diretamente, roda o jogar (evita executar no import)
if (__name__ == "__main__"):
    escolher_jogo()
