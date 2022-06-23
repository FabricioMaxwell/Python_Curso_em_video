print('=' * 11, 'LOJAS FABRÍCIO', '=' * 11)
preço = float(input('Preço das compras: R$'))

print("""FORMAS DE PAGAMENTOS
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] à 2x no cartão
[ 4 ] à 3x ou mais no cartão""")
opção = int(input('Qual é a opção? '))

if opção == 1:
    total = preço * 0.90
elif opção == 2:
    total = preço * 0.95
elif opção == 3:
    total = preço
    parcelas = preço / 2
    print(f'Sua compra será parcelada em 2x de R${parcelas:.2f} SEM JUROS.')
elif opção == 4:
    total = preço * 1.20
    qtd_parcelas = int(input('Quantas parcelas? '))
    parcelas = total / qtd_parcelas
    print(f'Sua compra será parcela em {qtd_parcelas}x de R${parcelas:.2f} COM JUROS.')
else:
    total = preço
    print('OPÇÃO INVALIDA de pagamento. TENTE NOVAMENTE!')   
print(f'Sua compra de R$ {preço:.2f} vai custar R${total:.2f} no final.')

