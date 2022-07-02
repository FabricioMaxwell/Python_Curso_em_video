frase = str(input('Digite uma frase: ')).upper().replace(' ', '')

inverter = frase[:: -1]

for c in inverter:
    print(f'O inverso de {frase} é {inverter}')

if frase == inverter:
    print('Temos um palímetro!')
else:
    print('A frase digitada não é um palíndromo!')