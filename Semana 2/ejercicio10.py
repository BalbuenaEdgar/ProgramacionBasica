

print('Invertir una Cadena\n')

textoUsuario = input('Ingrese un Texto: ')
textoInverso = ''

for letraU in textoUsuario:
    textoInverso = letraU + textoInverso
print(f'Texto invertido: {textoInverso}')