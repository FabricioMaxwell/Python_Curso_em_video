#Conversor de base númerica

n = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão: ')
print('''[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

base = int(input('Sua opção: '))

if base == 1:
    conversão = bin(n)[2:]
    numerico = 'BINÁRIO'
elif base == 2:
    conversão = oct(n)[2:]
    numerico = 'OCTAL'
elif base == 3:
    conversão = hex(n)[2:]
    numerico = 'HEXADECIMAL'
else:
    print('Opção invalida. TENTE NOVAMENTE!')
    conversão = 0
    numerico = 0
print(f'{n} convertido  para {numerico} é igual a {conversão}.')
