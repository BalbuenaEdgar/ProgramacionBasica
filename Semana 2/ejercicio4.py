

print('Números Fibonacci\n')

numeroUsuario = 0
contador = 0
x = 0
y = 1
while numeroUsuario <= 0 or numeroUsuario >= 51:
    numeroUsuario = int(input('Ingrese un numero del 1 al 50: '))

print((f'Se mostrarán {numeroUsuario} de la serie de Fibonacci'))

while contador < numeroUsuario:
    resultado = x + y
    x = y
    y = resultado

    print (f'{x}')
    contador += 1

    # 0 1 1 2 3 5 8 13 21 34