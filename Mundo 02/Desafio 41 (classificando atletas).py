from datetime import date

atual = date.today().year
nascimento = int(input('Ano de nascimento: '))

idade = atual - nascimento
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    classificação = 'MIRIM'
elif idade <= 14:
    classificação = 'INFANTIL'
elif idade <= 19:
    classificação = 'JÙNIOR'
elif idade <= 25:
    classificação = 'SÊNIOR'
else:
    classificação = 'MASTER'
print(f'Classificação: {classificação}')



