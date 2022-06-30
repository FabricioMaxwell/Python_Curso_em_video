t = int(input('Digite um número para ver sua tabuada: ' ))
m = 0

for c in range(1, 11):
    m = t * c
    print(f'{t} x {c:2.0f} = {m}')

