n = int(input('Digite um número: '))
divisivel = 0
for c in range(1, n + 1):
    if n % c == 0:
        print(f'\033[1;33m{c}\033[m', end=' ')
        divisivel += 1
    else:
        print(f'\033[1;91m{c}\033[m', end=' ')
print(f'\nO número {n} foi divisível {divisivel} vezes')

if divisivel == 2:
     print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')   