soma = 0
dados_clientes = {}

for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    dados_clientes[nome] = {
    "nome": nome
    "idade": idade
    "sexo": sexo    
    }
    
    soma += idade
    média = soma / p
    

print(f'A média de idade do grupo é de {média} anos.')
print(f'O homem mais velho tem {max(idade)} e se chama {nome[0]}')

