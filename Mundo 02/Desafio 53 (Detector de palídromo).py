frase = str(input('Digite uma frase: ')).strip().upper()

#gerar uma lista
palavras = frase.split()
#juntar a palavra
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')

if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')