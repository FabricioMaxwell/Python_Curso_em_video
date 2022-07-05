frase = str(input('Digite uma frase: ')).upper().replace(' ', '').strip()

inverter = frase[:: -1]

for c in inverter:
    print(f'{c}', end='')

if frase == inverter:
    print('\nTemos um palímetro!')
else:
    print('\nA frase digitada não é um palíndromo!')