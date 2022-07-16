print('Gerador de PA')
print('-=' * 12)

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))

termo = primeiro
cont = 1

while cont < 11:
     print(f'{termo}', end=' -> ' if cont < 10 else ' -> PAUSA')
     termo += razão
     cont += 1

