from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 a 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # jogador tenta adivinhar
computador = randint(0, 5) # faz o computador sortear entre 0 a 5
print('PROCESSANDO...')
sleep(1)
if jogador == computador:
    print('Pàrabéns! Você conseguiu me vencer!')
else:
    print(f'Ganhei! eu pensei no número {computador} e não no {jogador}!')
