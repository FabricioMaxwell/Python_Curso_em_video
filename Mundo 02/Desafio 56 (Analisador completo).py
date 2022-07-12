soma_idade = 0
média_idade = 0
maior_idade = 0
nome_velho = ''
total_mulher20 = 0

for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    
    soma_idade += idade 
    média_idade = soma_idade / 4

    if p == 1 and sexo in 'Mm':
        maior_idade = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade:
        maior_idade = idade
        nome_velho = nome
    if idade < 20 and sexo in 'Ff':
        total_mulher20 += 1    

print(f'A média de idade do grupo é de {média_idade} anos.')
print(f'O homem mais velho tem {maior_idade} e se chama {nome_velho}.')
print(f'Ao todo são {total_mulher20} mulheres com menos de 20 anos.')
