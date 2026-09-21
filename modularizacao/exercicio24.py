#Declaração de variáveis
valor: int = 0

def numDivisivel():
    if (valor % 2 == 0) and (valor % 3 == 0):
        print("O número é divisivel por 2 e 3")
    else:
        print("O número NÃO é divisivel por 2 e 3")

def main():
    global valor
    valor = int(input("Digite um valor: "))
    numDivisivel()

if (__name__ == '__main__'):
    main()