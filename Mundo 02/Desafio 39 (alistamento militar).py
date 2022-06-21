from datetime import date
atual = date.today().year

nascimento = int(input('Ano de nascimento: '))

idade = atual - nascimento
print(f'Quem nasceu {nascimento} tem {idade} anos em {atual}.')

if idade == 18:   
    print(f'Você tem que se alistar IMEDIATAMENTE!')
elif idade > 18:
    alistamento = idade - 18 
    print(f'Você já deveria ter se alistado há {alistamento} anos.')
    ano = atual - alistamento
    print(f'Seu alistamento foi em {ano}.')
else:
    alistamento = 18 - idade
    print(f'Ainda faltam {alistamento} anos para o alistamento.')
    ano = atual + alistamento
    print(f'Seu alistamento será em {ano}.')
