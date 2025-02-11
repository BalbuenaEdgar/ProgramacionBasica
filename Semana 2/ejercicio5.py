

print('Contar Vocales\n')

vocales = 'aeiou'
totalVocales = 0
textoUsuario = input('Ingrese un Texto: ').lower()

for letra in textoUsuario:
    for vocal in vocales:
        if vocal == letra:
            totalVocales += 1

print(f'Vocales en el texto ingresado: {totalVocales}')

'''
#Con funcion .count()
textoUsuario = input('Ingresa Texto: ')

a = textoUsuario.lower().count('a')
e = textoUsuario.lower().count('e')
i = textoUsuario.lower().count('i')
o = textoUsuario.lower().count('o')
u = textoUsuario.lower().count('u')
totalVocales = a + e + i + o + u

print('Vocales en el texto ingresado:')
print(f'A: {a}\nE: {e}\nI: {i}\nO: {o}\nU: {u}\nTotal: {totalVocales}')
'''