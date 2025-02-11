

print('Factorial de un Número\n')

numeroUsuario = 0
resultado = 1

while numeroUsuario <= 0 or numeroUsuario >= 20:
    numeroUsuario = int(input('Numero del 1 al 20: '))

numero_Usuario = numeroUsuario

for _ in range(numeroUsuario):
    resultado *= numeroUsuario
    numeroUsuario -= 1
print(f'{numero_Usuario}! = {resultado}')