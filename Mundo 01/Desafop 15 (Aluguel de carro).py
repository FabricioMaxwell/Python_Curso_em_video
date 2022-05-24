d = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))
pagar = (d * 60) + (km * 0.15)
print(f'O total a pagar é de R${pagar:.2f}')