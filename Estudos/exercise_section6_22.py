"""
Esse programa deve ler do usuário um número indeterminado de notas válidas no intervalo entre 10 e 20
e deverá mostrar a correspondente média aritmética. O programa deve se encerrar quando um número
inválido for digitado.
"""

contador = 0
soma = 0

while 1:
    nota = float(input("Digite uma nota: "))
    if nota >= 10 and nota <= 20:
        contador += 1
        soma += nota
    else:
        break 

print(f"A média aritmética das notas é: {round((soma/contador), 2)}")