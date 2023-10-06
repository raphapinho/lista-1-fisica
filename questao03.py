from vpython import *

# Definindo os vetores A e B
A = vector(2, 3, 4)
B = vector(3, -2, 2)

# a) Representação geométrica
scene = canvas(title="Representação  dos Vetores", width=800, height=600)
arrow_A = arrow(pos=vector(0, 0, 0), axis=A, color=color.red, shaftwidth=0.1)
arrow_B = arrow(pos=vector(0, 0, 0), axis=B, color=color.blue, shaftwidth=0.1)

# b) Vetor resultante da soma vetorial
result_soma = A + B
arrow_sum = arrow(pos=vector(0, 0, 0), axis=result_soma, color=color.green, shaftwidth=0.1)


# c) Vetor resultante da subtração vetorial
result_sub = A - B
arrow_subtract = arrow(pos=vector(0, 0, 0), axis=result_sub, color=color.orange, shaftwidth=0.1)


# d) Produto escalar e produto vetorial
prod_escalar = dot(A, B)
prod_vetorial = cross(A, B)

# Vetor resultante do produto vetorial 
vetor_resultante = arrow(pos=vector(0, 0, 0), axis=prod_vetorial, color=color.green, shaftwidth=0.1)

# printando resultados
print(f"Produto Escalar (A  x B): {prod_escalar}", prod_escalar)
print(f"Produto Vetorial (A x B): {prod_vetorial}")

scene.waitfor('click')
