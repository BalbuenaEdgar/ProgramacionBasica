

print('Suma de Digitos\n')

numeroUsuario = input('Ingresa un numero: ')
suma = 0

for numero in numeroUsuario:
    suma += int(numero)

print(f'La suma de los digitos del numero {numeroUsuario} es: {suma}')