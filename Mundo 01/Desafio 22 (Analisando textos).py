nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
separa = nome.split()
#print('Seu primeiro nome é {} e tem {} letras'.format(nome[0:8], nome.find(' ')))
print(f'Seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras')


