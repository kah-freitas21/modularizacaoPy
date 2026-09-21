#Declaração de variáveis
nota1: float = 0
nota2: float = 0
nota3: float = 0
nota4: float = 0
media: float = 0

def mediaNota():
    global media
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print("Sua média é: ", media)

    if (media >= 6):
        print("Você está aprovada!")
    elif (media >= 3 and media <6):
        print("Você terá que realizar o exame.")
    else: 
        print ("Você está retido.")


def main():
    global nota1
    global nota2
    global nota3
    global nota4

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))

    mediaNota()
if (__name__ == '__main__'):
    main()