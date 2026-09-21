#Declaração de variáveis
num1: int = 0
num2: int = 0
maior: int = 0
menor: int = 0

def multiploNum():
    global maior
    global menor
    if ( num1 > num2):
        maior = num1
        menor = num2
    else:
        maior = num2
        menor = num1

    if (maior % menor == 0):
        print("O maior número é multiplo do menor.")
    else:
        print("O maior número NÃO é multiplo do menor.")


def main():
    global num1
    global num2
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    multiploNum()

if (__name__ == '__main__'):
    main()