""" Jogo da Forca """

from random import choice


def escolher_palavra():
    """Função que escolhe uma palavra aleatória da lista de palavras."""
    palavras = [
        "desenvolvimento",
        "tecnologia",
        "python",
        "logica",
        "dados",
        "algoritmo",
        "computador",
        "internet",
        "software",
    ]
    return choice(palavras)


def exibir_forca(chances):
    """Função que exibe a forca com base no número de erros."""
    chances = int(chances)
    print(f"{'=' * 30} Jogo da Forca {'=' * 30}\n")
    print(f"{'=' * 28} Você tem {chances} chances {'=' * 27}\n\n")


def jogar():
    """Função principal que controla o jogo da forca."""
    palavra = escolher_palavra()
    letras_certas = ["_"] * len(palavra)
    chances = 6

    while chances > 0:
        exibir_forca(chances)
        print(f"Palavra: {' '.join(letras_certas)}\n")
        letra = input("Digite uma letra: ")

        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_certas[i] = letra
        else:
            chances -= 1

        if "_" not in letras_certas:
            print(f"Parabéns! Você acertou a palavra: {palavra}")
            break

    if chances == 0:
        print(f"Você perdeu! A palavra era: {palavra}")
