#Declaração de variáveis
coeficienteA: float = 0
coeficienteB: float = 0
coeficienteC: float = 0
delta: float = 0
x1: float = 0
x2: float = 0

def equacao():
    global delta
    global x1
    global x2
    if (coeficienteA == 0):
        print ("Não é uma equação do 2º grau.")
    else:
        delta = (coeficienteB * coeficienteB) - (4 * coeficienteA * coeficienteC)
        if( delta >= 0):
            x1 = (-coeficienteB + (delta ** 0.5)) / (2 * coeficienteA)
            x2 = (-coeficienteB - (delta ** 0.5)) / (2 * coeficienteA)
            print("Suas raízer reais são:", x1, "e ", x2)
        else:
            print("Não possui raízes reais.")

def main ():
    global coeficienteA
    global coeficienteB
    global coeficienteC

    coeficienteA = float(input("Digite o valor do coeficiente A: "))
    coeficienteB = float(input("Digite o valor do coeficiente B: "))
    coeficienteC = float(input("Digite o valor do coeficiente C: "))
    equacao()

if (__name__ == '__main__'):
    main()