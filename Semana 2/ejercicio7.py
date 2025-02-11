

print('Suma de Elementos en una Lista\n')

tamLista = 0
listaNumeros = []
sumaTotal = 0

while tamLista <= 0:
    tamLista = int(input('Total de numeros a ingresar: '))

while tamLista > 0:
    listaNumeros.append(float(input('Ingrese el Numero: ')))
    tamLista -= 1

for numero in listaNumeros:
    sumaTotal += numero

print(f'Suma total de los numeros ingresados: {sumaTotal}')
