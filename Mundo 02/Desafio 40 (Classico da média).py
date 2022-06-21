primeira_nota = float(input('Primeira nota: '))
segunda_nota = float(input('Segunda nota: '))

media = (primeira_nota + segunda_nota) / 2
print(f'A nota foi de {primeira_nota} e {segunda_nota}, a média do aluno é {media:.1f}.')

if media < 5:
    print('O aluno está REPROVADO!')
elif 7 > media >= 5:
    print('O aluno está em RECUPERAÇÃO!')
else:
    print('O aluno está APROVADO!')





