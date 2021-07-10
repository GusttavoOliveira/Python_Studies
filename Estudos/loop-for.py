"""
Exemplo:

for item in iteravel:
    #instruções do loop

Dessa forma percebe-se que o for trabalha se repetindo sobre objetos ou sequencias iteráveis
"""


nome = 'Luiz Gusttavo'
lista = {1, 2, 3, 4, 5, 6}

# Para fazer um loop dentro de um iterável criaremos uma variávei para assumir
# A posição de cada objeto dentro do iterável e "se transformar" naquele elemento do iterável
# Parecido com o for_each do c++

# Iterando sobre o nome
for letra in nome:
    print(letra)

"""
Exemplos de possíveis iteráveis

- Lista:
numeros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

- String:
nome_funcionario = 'Marcos Andrade'

- Range:
numeros = range(1, 10) -> Lembrando que o range não conta o último número

OBS: range(valor_inicial, valor_final) <-> mas o valor_final não incluso
"""
 