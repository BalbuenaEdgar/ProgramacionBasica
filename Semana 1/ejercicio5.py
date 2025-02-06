
print('Calculadora de Descuento')

precio = float(input('\nIngrese el precio del producto: '))
descuento = float(input('Ingrese el porcentaje de descuento: '))
porcentaje = descuento*.01
total = (precio - (precio*porcentaje))

print(f'\nPrecio Final: {total}')
