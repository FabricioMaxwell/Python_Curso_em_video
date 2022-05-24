import math
g = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(g))
cosseno = math.cos(math.radians(g))
tan = math.tan(math.radians(g))
print(f'O ângulo de {g} tem o SENO de {seno:.2f}')
print(f'O ângulo de {g} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {g} tem a TANGENTE de {tan:.2f}')