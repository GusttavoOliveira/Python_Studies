"""
Listas em Python funcionam como vetores/matrizes(arrays) em outras linguagens com a diferença de serem DINAMICOS 
e de poderem guardar QUALQUER TIPO DE DADO

- Dinâmico: Não possui tamanho fixo, simplesmente criamos a lista e vamos adicionamos elementos. O limite de bytes é a sua memória;
- Não possuem tipo de dado fixo: Podem armazenar qualquer tipo de dado em qualquer posição.

-> Listas são representadas por []

"""


# Exemplo:

minha_lista = [5, 10 ,6, 8, 79, 1000, 15]

minha_lista2 = ['L', 'u', 'i','z', ' ', 'G', 'u', 's', 't', 't', 'a', 'v', 'o']

minha_lista3 = []

minha_lista4 = [range(11)]

minha_lista5 = ['Luiz Gusttavo']

# As listas 5 e 2 são exatamente iguais #

# Podemos facilmente verificar se um valor está contido em uma lista usando o 'in'

if 'u' in minha_lista2:
    print("Achei!\n")       # Para de procurar ao achar o primeiro 'u' da lista
else:
    print("Não achei!\n")

"""
Relembrando:
    * Podemos usar os comandos 'dir' e 'help' no console seguidos da palavra 'list' para ver os métodos que podemos utilizar com listas
      e uma descrição do Python sobre listas respectivamente usando esses comandos.
    * Para usar um método numa lista basta escrever o nome da lista seguido de ponto e o nome do método com os parâmetros necessários
      
      ex: minha_lista5.sort()

    Algumas das funções e métodos mais usados e mais legais de serem usados são:
    
        sort() -> Ordena a lista de maneira crescente.
        count(object) -> Conta quantos objetos iguais ao passado como parâmetro existem dentro da lista.
        append(object) -> Adiciona um elemento no final da lista (Com append só conseguimos adicionar um elemento por vez. COntudo conseguimos adicionar uma lista dentro de outra lista)
        extend(iterable) -> Adiciona mais de um elemento ao final da lista (Não aceita valores únicos, aceita apenas iteráveis (listas, strings, ranges, ...))
        insert(position, object) -> Insere um valor na lista em uma posição predeterminada sem fazer substituições. Se houver um elemento na posição indicada ele é deslocado para a posição seguinte
        reverse() -> Inverte os elementos da lista
        copy() -> Copia o conteúdo da lista para colocar em outro lugar
        len(list) -> Retorna o tamanho da lista
        sum(list) -> Retorna a soma dos elementos da lista
        max(list) -> Retorna o maior elemento da lista
        min(list) -> Retorna o menor elemento da lista
        pop() -> Remove o último elemento da lista. Também retorna esse último elemento.
        pop(index) -> Remove o elemento da lista no índice passado. Também retorna esse elemento.
        clear() -> Limpa a lista tornando-a uma lista vazia
        ...

    Operadores como '+', '*' e operadores lógicos também funcionam com listas.
    lista1 = ['L', 'u']
    lista2 = ['i', 'z']
    lista3 = lista1 + lista2    # lista3 = ['L', 'u', 'i', 'z']

    lista3 = lista3 * 3         # lista3 = ['L', 'u', 'i', 'z', 'L', 'u', 'i', 'z', 'L', 'u', 'i', 'z']


"Shallow copy" e "Deep copy"

Deep copy:
  Ao utilizarmos o método copy() para crirarmos uma listaNova cópia de uma listaAntiga, as duas listas são independentes e tudo que modificamos
  em uma delas não afeta a outra. Em Python isso se chama Deep Copy(Cópia Profunda)

Shallow copy: 
  Ao utilizarmos o operador de atribuição " = " para fazermos uma atribuição de uma lista em outra lista, as duas listas criadas ficam atreladas
  uma à outra e tudo que for modificado em uma também será modificado na outra. Em Python isso se chama Shallow Copy(Cópia Rasa)


    
"""