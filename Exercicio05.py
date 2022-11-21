ficha = list()

# Armazena os dados do aluno na ficha
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 01: '))
    nota2 = float(input('Nota 02: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    prosseguir = str(input('Deseja prosseguir? [S/N] '))
    if prosseguir in 'Nn':
        break

# Imprime uma tabela com os dados

for i, a in enumerate(ficha):
    print(f'{i} {a[0]} {a[2]}')
