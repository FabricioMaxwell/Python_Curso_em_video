sal = float(input('Qual é o salário do funcionário R$ '))
if sal <= 1250:
    sal_novo = sal + (sal * 15 / 100)
else:
    sal_novo = sal + (sal * 10 / 100)
print(f'Quem ganha \033[36mR${sal:.2f}\033[m passa a ganhar \033[34mR${sal_novo:.2f}\033[m agora.')