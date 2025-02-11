

print('Ordenar una Lista\n')

tamLista = 0
listaNumeros = []
listaOrdenada = []

while tamLista <= 0:
    tamLista = int(input('Total de numeros a ingresar: '))

while tamLista > 0:
    listaNumeros.append(float(input('Ingrese el Numero: ')))
    tamLista -= 1

listaNumeros.sort()

print(f'Numeros ingresados acomodados de menor a mayor: \n{listaNumeros}')