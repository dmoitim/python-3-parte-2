import random


def jogar():
    print("*************************************")
    print("* Bem vindo ao jogo de Adivinhação! *")
    print("*************************************")

    total_de_tentativas = 0
    numero_secreto = random.randrange(1, 101)
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil   (2) Médio   (3) Difícil")

    nivel = int(input("Defina o nível desejado: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute = int(input("Digite o seu número ente 1 e 100: "))
        print("Você digitou", chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100.")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("O seu chute foi maior que o número secreto.")
            elif (menor):
                print("O seu chute foi menor que o número secreto")

            # abs - número absoluto
            pontos_perdidos = abs(chute - numero_secreto)
            pontos = pontos - pontos_perdidos

            if (rodada == total_de_tentativas):
                print("O número secreto era {}. Você fez {}".format(
                    numero_secreto, pontos))

    print("Fim do jogo!")


# Se o arquivo foi executado diretamente, roda o jogar (evita executar no import)
if (__name__ == "__main__"):
    jogar()
