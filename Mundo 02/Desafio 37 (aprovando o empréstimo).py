#Aprovando o empréstimo

valor_casa = float(input('Valor da casa: R$ '))
salário = float(input('Salário do comprador: R$ '))
anos_financiamento = int(input('Quantos ano de financiamento: '))

mensal = anos_financiamento * 12
parcela_mensal = valor_casa / mensal

if parcela_mensal <= salário * 0.30:
    prestação = parcela_mensal
    print('Empréstimo APROVADO!')
else:
    prestação = parcela_mensal
    print('Empréstimo NEGADO!')
print(f'Para pagar uma casa de R$ {valor_casa:.2f} em {anos_financiamento} anos a prestação será de R$ {prestação:.2f}.')
    
    
