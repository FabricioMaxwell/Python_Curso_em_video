from random import randint
from time import sleep

print('-=' * 12, 'BEM VINDO AO JO KEN PO!', '-=' * 12)

print("""Sua opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jogador = int(input('Qual é a sua jogada? '))
opçoes = ['pedra', 'papel', 'tesoura']
computador = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')


if computador == jogador: # Jogaram iguais
    print('EMPATE')

elif computador == 0: #Computador jogou Pedra
    if jogador == 1:
        print('-=' * 12)
        print(f'Computador jogou {opçoes[computador]}')
        print(f'Jogador jogou {opçoes[jogador]}')
        print('-=' * 12)
        print('jOGADOR VENCE!')
    else:
        print('-=' * 12)
        print(f'Computador jogou {opçoes[computador]}')
        print(f'Jogador jogou {opçoes[jogador]}')
        print('-=' * 12) 
        print('COMPUTADOR VENCE!')

elif computador == 1: #Computador jogou Papel
    if jogador == 0:
        print('-=' * 12)
        print(f'Computador jogou {opçoes[computador]}')
        print(f'Jogador jogou {opçoes[jogador]}')
        print('-=' * 12)
        print('COMPUTADOR VENCE!')
    else:
        print('-=' * 12)
        print(f'Computador jogou {opçoes[computador]}')
        print(f'Jogador jogou {opçoes[jogador]}')
        print('-=' * 12)
        print('JOGADOR VENCE!')

elif computador == 2: #Computador jogou Tesoura
    if jogador == 1:
        print('-=' * 12)
        print(f'Computador jogou {opçoes[computador]}')
        print(f'Jogador jogou {opçoes[jogador]}')
        print('-=' * 12)
        print('COMPUTADOR VENCE!')
    else:
        print('-=' * 12)
        print(f'Computador jogou {opçoes[computador]}')
        print(f'Jogador jogou {opçoes[jogador]}')
        print('-=' * 12)
        print('JOGADOR VENCE')

else:
    print('JOGADA INVÁLIDA!')

