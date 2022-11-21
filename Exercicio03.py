matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

valoresPares = []
valorMaior = somaColuna = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {l, c}: '))
        if matriz[l][c] % 2 == 0:
            valoresPares.append(matriz[l][c])

for l in range(0, 3):
    somaColuna += matriz[l][2]

for c in range(0, 3):
    if matriz[1][c] > valorMaior:
        valorMaior = matriz[1][c]

for linha in matriz:
    print(linha)

print(f"Soma dos valores pares: {sum(valoresPares)}")
print(f'A soma dos valores da terceira coluna é: {somaColuna}')
print(f'O maior valor da segunda linha é: {valorMaior}')
