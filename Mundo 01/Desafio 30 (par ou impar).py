n = int(input('Me diga um número qualquer: '))
resto = n % 2
if resto == 0:
    print(f'O número \033[35m{n}\033[m é par!')
else:
    print(f'O número \033[31m{n}\033[m é impar!')
