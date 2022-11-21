listaPrincipal = [[], []]
valorInput = 0

for i in range(1, 8):

    valorInput = int(input(f'Digite o {i}o. valor inteiro: '))

    if valorInput % 2 == 0:
        listaPrincipal[0].append(valorInput)
    else:
        listaPrincipal[1].append(valorInput)

print(sorted(listaPrincipal[0]))
print(sorted(listaPrincipal[1]))
