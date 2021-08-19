"""
PUCPR - ANALISE E DESENVOLVIMENTO DE SISTEMAS
ALUNO: MATHEUS BAKAUS BRUNO
MATERIA: RACIOCÍNIO COMPUTACIONAL
"""
from random import randint

shots = 0
brains = 0
steps = 0

# DEFININDO DADOS
# T = TIROS, C = CEREBROS, P = PASSOS

diceGreen = 'CPCTPC'
diceYellow = 'TPCTPC'
diceRed = 'TPTCPT'

copo = []
pontos = []

for i in range(0, 6):
    copo.append(diceGreen)

for i in range(0, 4):
    copo.append(diceYellow)

for i in range(0, 3):
    copo.append(diceRed)

print('Mostrar dados no copo')

for i in copo:
    # print(i)

    while True:
        numPlayer = int(input('Quantos players nessa rodada, caro aventureiro?\n'))

        if numPlayer > 1:
            print('================================INICIANDO JOGO=========================================')

        listPlayers = []
        for ind in range(0, numPlayer):
            nome = input('Como se chama, caro aventureiro?\n')
            cerebros = 0
            tiros = 0
            player = [ind, nome, cerebros, tiros]
            listPlayers.append(player)

        for x in range(0, 3):
            # INDICE ALEATÓRIO
            randomNumber = randint(0, 12)
            # DADO SORTEADO
            dicePlayer = copo[randomNumber]
            # FACE DADO
            diceFace = randint(0, 5)

            if dicePlayer[diceFace] == "C":
                print('--------------------------------\n\n\n... CEREBRO!... \n Você comeu um cérebro')
                brains = brains+1
            elif dicePlayer[diceFace] == "T":
                print('--------------------------------\n\n\n... TIRO!... \n Você levou um tiro!')
                shots = shots + 1
            else:
                print('--------------------------------\n\n\n... PASSOS!... \n a vitima escapou')
                steps = steps + 1
