
print('Clasificación de Edad')

edad = int(input('\nIngrese su edad: '))

if (edad < 12):
    print('\nEs un Niño')
elif (edad < 18):
    print('\nEs un Adolescente')
elif (edad < 60):
    print('\nEs un Adulto')
else:
    print('\nEs un Adulto Mayor')