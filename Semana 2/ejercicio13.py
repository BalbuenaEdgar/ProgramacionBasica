
print('Contar Caracteres\n')

textoUsuario = input('Ingrese un texto: ').lower()
caracterElegido = input('Elige un caracter: ')
contadorCaracter = 0

for caracter in textoUsuario:
    if caracter == caracterElegido:
        contadorCaracter += 1

cantidadVeces = '1 vez' if contadorCaracter == 1 else f'{contadorCaracter} veces'

print (f'El caracter {caracterElegido} aparece {cantidadVeces}')