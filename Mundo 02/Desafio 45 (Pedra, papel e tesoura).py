from random import choice
from time import sleep
print("""Sua opções
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA""")
jogada = int(input('Qual é a sua jogada? '))
opçoes = ['pedra', 'papel', 'tesoura']
computador = choice(opçoes)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')

pedra = 1
papel = 2
tesoura = 3

if jogada == 1 and computador == 3 or jogada == 2 and computador == 1 or jogada == 3 and computador == 2:
    jogador = 'JOGADOR VENCE'
print('-=' * 12)
print(f'Computador jogou {computador}')
print(f'Jogador jogou {jogada}')
print('-=' * 12)


