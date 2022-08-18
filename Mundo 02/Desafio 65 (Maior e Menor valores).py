resposta = 'S'
cont = 0
soma = 0
while resposta in 'Ss':
    numero = float(input('Digite um número: '))
    cont += 1
    soma += numero
    media = soma / cont
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if menor < menor:
            menor = numero
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
print(f'Você digitou {cont} números e a média foi de {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')



