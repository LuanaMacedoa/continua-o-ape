numeros = 0
for i in range(6):
    n = int(input(f'Digite a nota: '))
    numeros += n
media = numeros/6
print(f'{media:.2f}')