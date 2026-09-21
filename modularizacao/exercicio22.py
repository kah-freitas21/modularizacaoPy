#Declaração de variáveis
valor1: int = 0
valor2: int = 0

def ordemCrescente():
    if (valor1 > valor2):
        print("A ordem crescente é: ", valor2, "e", valor1)
    else:
        print("A ordem crescente é: ", valor1, "e", valor2)

def main():
    global valor1
    global valor2

    valor1 = int(input("Digite o valor 1: "))
    valor2 = int(input("Digite o valor 2: "))
    ordemCrescente()

if (__name__ == '__main__'):
    main()