
print('Calculadora de Año Bisiesto')

año = int(input('\nIngrese el año: '))

if ((año % 4 == 0) and (año % 100 != 0) or (año % 400 == 0)):
    print(f'\nEl Año {año} es Bisiesto')
else:
    print(f'\nEl Año {año} no es Bisiesto')
