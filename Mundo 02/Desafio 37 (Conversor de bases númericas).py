n = int(input('Digite um número inteiro: '))

print(f'''
Escolha uma das bases para conversão
[ 1 ] converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] converter para HEXADECIMAL 
''')

opção = int(input('Sua opção: '))

if opção == 1:
    conversão = bin(n)[2:]
    base = 'BINÀRIO'
elif opção == 2:
    conversão = oct(n)[2:]
    base = 'OCTAL'
elif opção == 3:
    conversão = hex(n)[2:]
    base = 'HEXADECIMAL'
else:
    print('Sua opção é inválida. TENTE NOVAMENTE')
print(f'{n} convertido para {base} é igual a {conversão}')