#Declaração de variáveis
valor1: int = 0
valor2: int = 0
maior: int = 0
menor: int = 0
diferenca: int = 0

def difMaiorMenor():
    global maior
    global menor
    global diferenca

    if(valor1 > valor2):
        maior = valor1
        menor = valor2
    else:
        maior = valor2
        menor = valor1
    diferenca = maior - menor
    print("A diferença dos valores é: ", diferenca)

def main():
    global valor1
    global valor2
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    difMaiorMenor()

if (__name__ == '__main__'):
    main()