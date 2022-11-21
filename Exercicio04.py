import random
import time

listaJogadas = list()
jogadas = int(input("Quantas jogadas você quer sortear? "))

for j in range(jogadas):
    listaPalpites = []
    for num in range(6):
        while True:
            numero = random.randint(1, 60)
            if numero not in listaPalpites:
                listaPalpites.append(numero)
                break

    listaJogadas.append(sorted(listaPalpites))

print('=-' * 3 + f' SORTEANDO {jogadas} JOGADAS! ' + '=-' * 3)

for j in range(jogadas):
    time.sleep(1)
    print(f'Jogo {j + 1}: {listaJogadas[j]}')

