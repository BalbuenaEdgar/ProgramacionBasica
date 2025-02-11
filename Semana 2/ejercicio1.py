

print('Suma de Números Pares\n')

suma = 0
for _ in range(101):
    if (_ % 2) == 0:
        suma += _
print(f'La suma de los numeros pares del 1 al 100 es: {suma}')