distancia = float(input('Qual é a distância da sua viagem? '))
print(f'Você está preste a começar uma viagem de {distancia:.1f}Km')
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45 # metodo simplificado
#if distancia <= 200:
    #preço = distancia * 0.50
#else:
    #preço = distancia * 0.45
print(f'E o preço da sua passagem será de R${preço:.2f}.')
