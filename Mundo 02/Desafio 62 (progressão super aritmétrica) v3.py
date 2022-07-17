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


          if termo2 != 0: 
               termo2 = int(input('\nQuantos termo você quer mostrar mais? '))
               print(f'\n{termo2} ->', end=' PAUSA ')
               termo2 += razão
               cont += 1
          else:
               print(f'\nProgressão finalizada com {cont} termos mostrados.')