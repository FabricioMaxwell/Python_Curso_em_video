vel = float(input('Qual a velocidade atual do carro? '))
if vel > 80:
    print('Multado! Você exedeu o limite permitido que é de 80Km/h.')
    multa = (vel - 80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}!')
print('Tenha um bom dia! Digija com segurança!')
