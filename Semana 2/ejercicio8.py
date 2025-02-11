

print('Encontrar el Mayor y Menor en una Lista\n')

tamLista = 0
listaNumeros = []

while tamLista <= 0:
    tamLista = int(input('Total de numeros a ingresar: '))

while tamLista > 0:
    listaNumeros.append(float(input('Ingrese el Numero: ')))
    tamLista -= 1

print(f'Número Mayor: {max(listaNumeros)}\nNúmero Menor: {min(listaNumeros)}')