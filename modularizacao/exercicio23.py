#Declaração de variáveis
valorCrescente1: float = 0
valorCrescente2: float = 0
valorCrescente3: float = 0
numero: float = 0

def ordemCrescente():
    if (numero <= valorCrescente1):
        print("A ordem crescente é: ", numero, ",",valorCrescente1, ",", valorCrescente2, ",", valorCrescente3)
    elif(numero <= valorCrescente2):
        print("A ordem crescente é: ", valorCrescente1,",", numero, ",", valorCrescente2, ",", valorCrescente3)
    elif(numero <= valorCrescente3):
            print("A ordem crescente é: ", valorCrescente1,",", valorCrescente2, ",",numero,",", valorCrescente3)
    else:
         print("A ordem crescente é: ", valorCrescente1, ",", valorCrescente2, ",", valorCrescente3, ",", numero)


def main():
    global valorCrescente1
    global valorCrescente2
    global valorCrescente3
    global numero

    valorCrescente1 = float(input("Digite o primeiro valor em ordem crescente: "))
    valorCrescente2 = float(input("Digite o segundo valor em ordem crescente: "))
    valorCrescente3 = float(input("Digite o terceiro valor em ordem crescente: "))
    numero = float(input("Digite um valor qualquer: "))

    ordemCrescente()


if (__name__ == '__main__'):
    main()