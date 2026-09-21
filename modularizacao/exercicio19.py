#Declaração de variáveis
valor1: float = 0
valor2: float = 0
maior: float = 0

def maiorMenor():
    global maior
    if (valor1 > valor2):
        maior = valor1
    else:
        maior = valor2
    print("O maior valor é: ", maior)

def main():
    global valor1
    global valor2
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    maiorMenor()

if (__name__ == '__main__'):
    main()