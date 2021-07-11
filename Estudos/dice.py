"""
Esse programa vai gerar números aleatórios à medida que o usuário pedir
Números de 1 a 6.
"""


import random

print('--------------- DADO DA SORTE ---------------\n')

# Laço principal do programa
while 1:
    
    print('Digite quantas faces o seu dado terá: ',  end='')
    faces = input()
    
    # Verifica se a entrada foi um número inteiro
    if faces.isdecimal():
        faces = int(faces)
        print('\nJogando dados...\n')
        resultado = random.randint(1, faces)
        print(f'O resultado foi: {resultado}')
    else:
        print('Tentativa inválida!')
        continue

    # Verificação para saber se o usuário deseja jogar o dado mais uma vez
    print('\nQuer jogar outra vez? (s/n)', end='')
    resposta = input()

    if resposta == 's' or resposta == 'S':
        continue
    elif resposta == 'n' or resposta == 'N':
        break
    else:
        print('Resposta inválida interpretada como não!')
        break