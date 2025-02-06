
print('Calculadora de IMC')

peso = float(input('\nIngrese su Peso (kg): '))
altura = float(input('Ingrese su Altura (metros): '))
imc = (peso / (altura**2))

print(f'\nEl IMC es: {imc}')