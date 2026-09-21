#Declaração de variáveis
horaInicio: int = 0
horaFinal: int = 0
minutoInicio: int = 0
minutoFinal: int = 0
hora: int = 0
minuto: int = 0

def horaJogo():
    global hora
    global minuto
    global horaFinal
    global minutoFinal
    if (horaFinal < horaInicio):
        horaFinal = horaFinal + 24
    if (minutoFinal < minutoInicio):
        minutoFinal = minutoFinal + 60
        horaFinal = horaFinal - 1
    hora = horaFinal - horaInicio
    minuto = minutoFinal - minutoInicio
    print("O jogo durou ", hora, " horas e", minuto, " minutos.")

def main():
    global horaInicio
    global horaFinal
    global minutoInicio
    global minutoFinal
    horaInicio = int(input("Digite a hora de início do jogo: "))
    minutoInicio = int(input("Digite o minuto de início do jogo: "))
    horaFinal = int(input("Digite a hora final do jogo: "))
    minutoFinal = int(input("Digite o minuto final do jogo: "))
    horaJogo()


if (__name__ == '__main__'):
    main()