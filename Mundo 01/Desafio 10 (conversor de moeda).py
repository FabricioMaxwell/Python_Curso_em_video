reais = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = reais / 4.80
euros = reais / 5.16
print(f'Com R${reais:.2f} você pode comprar US${dolar:.2f} e E$ {euros:.2f}')