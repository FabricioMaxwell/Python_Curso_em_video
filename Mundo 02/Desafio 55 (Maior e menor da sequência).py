pesos = []

for p in range(1, 6):
    peso = float(input(f'O peso da {p}º pessoa: '))
    pesos.append(peso)

maior = max(pesos)
menor = min(pesos)

print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')