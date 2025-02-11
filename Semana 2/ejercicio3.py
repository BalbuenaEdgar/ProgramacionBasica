

print('Números Primos\n')

numeroUsuario = int(input('Introduce un numero: '))
primo = False

for _ in range(2, numeroUsuario, 1):
    if ((_ != 1) or (_ != numeroUsuario)):
        if numeroUsuario % _ == 0:
            print(f'El numero {numeroUsuario} no es primo')
            break
        else:    
            primo = True
            
if primo:
        print(f'El numero {numeroUsuario} es primo')