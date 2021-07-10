"""
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. 
Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, 
caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". 
Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem 
correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.
"""


import math

coef1 = input()
coef2 = input()
coef3 = input()

coef1 = float(coef1)
coef2 = float(coef2)
coef3 = float(coef3)

delta = (coef2**2) - (4*coef1*coef3)

if delta < 0 or coef1 == 0:
    print("Impossivel calcular")

elif delta >= 0:
    r1 = ((-coef2) + math.sqrt(delta)) / (2*coef1)
    r2 = ((-coef2) - math.sqrt(delta)) / (2*coef1)

    print(f"R1 = {round(r1, 5)}")
    print(f"R2 = {round(r2, 5)}")
    
