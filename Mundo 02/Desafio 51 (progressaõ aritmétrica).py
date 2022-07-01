print('=' * 18)
print('10 TERMO DE UMA PA')
print('=' * 18)

n = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

décimo = n + (11 - 1) * razao
for c in range(n, décimo, razao):
    print(c, end=' -> ')
print('ACABOU')

