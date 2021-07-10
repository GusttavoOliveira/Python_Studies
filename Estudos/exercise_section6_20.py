"""
Esse programa deve ler uma sequencia indeterminada de numeros inteiros e informar se eles são pares
ou não. Além disso deverá informar a quantidade de números lidos e quantos deles são pares.
O processo termina quando o usuário digitar o número 1000.
"""


contador = 0
conta_par = 0

while 1:
    num = input("Informe um valor: ")
    
    try:
        if(int(num) == 1000):
            print("O programa acabou!\n")
            break
        elif((int(num) % 2) == 0):
            contador += 1
            conta_par += 1
            print("É par!\n")
        else:
            contador += 1
            print("Não é par!\n")
    except:
        print("Insira um número válido.\n")

print(f"O programa teve {contador} entradas.\nDas quais {conta_par} eram pares!\n")