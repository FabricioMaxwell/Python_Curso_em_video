print('Gerador de PA')
print('-=' * 12)

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))

termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
     total += mais
     while cont <= total:
          print(f'{termo} ->', end=' ')
          termo += razão
          cont += 1
     print('PAUSA')
     mais = int(input('Quantos termos você quer mostrar mais? '))
print(f'Progresso finalizado com {total} termos mostrados.')