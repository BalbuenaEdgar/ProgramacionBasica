

print('Contar Palabras\n')

textoUsuario = ''

while textoUsuario == '':
    textoUsuario = input('Ingrese un Texto: ').strip()

contadorEspacio = 0

for caracter in textoUsuario:
    if caracter == ' ':
        contadorEspacio += 1

cantidadPalabras = f'1' if contadorEspacio == 0 else f'{contadorEspacio + 1}'

print(f'Cantidad de palabras en el texto ingresado: {cantidadPalabras}')
