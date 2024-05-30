""" Calculadora simples com quatro operações matemáticas. """


def adicionar(x, y):
    """Função que soma dois números"""
    return x + y


def subtrair(x, y):
    """Função que subtrai dois números"""
    return x - y


def multiplicar(x, y):
    """Função que multiplica dois números"""
    return x * y


def dividir(x, y):
    """Função que divide dois números"""
    if y == 0:
        raise ValueError("Não é possível dividir por zero")
    return x / y


operacoes = {"1": adicionar, "2": subtrair, "3": multiplicar, "4": dividir}

while True:
    print("\nEscolha uma operação:")
    print("1. Adicionar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair \n")

    escolha = input("Digite o número da operação desejada: ")

    if escolha == "5":
        print("Obrigada por utilizar a calculadora!")
        break

    if escolha in operacoes:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        funcao = operacoes[escolha]
        resultado = funcao(num1, num2)

        print(f"O resultado é: {resultado}")
    else:
        print("Escolha inválida, tente novamente.")
