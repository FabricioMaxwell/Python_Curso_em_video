from pickletools import TAKEN_FROM_ARGUMENT8U


print('GERADOR DE PA')
print('-=' * 15)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razãoo da PA: '))

cont = 1
termo = primeiro
while cont < 11:
    print(f'{termo}', end=' -> ')
    termo += razão
    cont += 1
print('FIM!', end='')
    
