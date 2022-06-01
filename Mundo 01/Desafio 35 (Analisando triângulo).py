print('-=' * 15)
print('Analisador de Triângulo')
print('-=' * 15)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < b + a:
    triangulo = 'ṔODEM FORMAR'
else:
    triangulo = 'NÃO PODEM FORMAR'
print(f'Os segmentos acima {triangulo} triângulo!')

