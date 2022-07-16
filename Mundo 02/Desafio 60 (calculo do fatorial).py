print('Digite um número para')
n = int(input('Calcular seu fatorial: '))

fatorial = 1

print(f'Calculando {n}! = ', end='')

while n > 0:
    print(f'{n}', end='')
    print(' x ' if n > 1 else ' = ', end='')
    fatorial *= n
    n -= 1
print(f'{fatorial}', end='')