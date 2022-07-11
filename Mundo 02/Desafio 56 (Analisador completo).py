soma_idade = 0
média_idade = 0
maior_idade = 0
nome_velho = ''

for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    
    soma_idade += idade 
    média_idade = soma_idade / 4

    if p == 1 and sexo in 'Mn':
        maior_idade = idade
        nome_velho = nome
    else:
        
        


print(f'A média de idade do grupo é de {} anos.')
print(f'O homem mais velho tem {} e se chama {}')

