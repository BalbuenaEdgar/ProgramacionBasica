
print('Conversión de Temperaturas')

tempCelsius = int(input('\nIngrese la Temperatura en grados Celsius: '))
tempFahrenheit = ((tempCelsius * 9/5) + 32) 
tempKelvin = (tempCelsius + 273.15)

print(f'\n\nTemperatura en grados Fahrenheit: {tempFahrenheit}')
print(f'Temperatura en grados Kelvin: {tempKelvin}')