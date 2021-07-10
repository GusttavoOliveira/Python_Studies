"""
Esse programa vai ler as notas de 3 alunos e vai retornar
um boletim parcial dizendo se os alunos foram aprovados, reprovados ou 
se vão ficar de recuperação

Critérios:
nota maior que 7, aprovado
nota entre 5 e 7, recuperação
nota menor do que 5, reprovado
"""


print("Olá professor Luiz Gusttavo! Cadastre 3 alunos para calcularmos suas médias.\n")

for n in range(3):
    nome = input("Qual é o nome do aluno? ")
    nota1 = input(f"Qual é a primeira nota de {nome}? ")
    nota2 = input(f"Qual é a segunda nota de {nome}? ")
    nota3 = input(f"Qual é a terceira nota de {nome}? ")
    
    if(n == 0):
        media1 = (float(nota1) + float(nota2) + float(nota3)) / 3.0
        
        if(media1 >= 7):
            final1 = "Aprovado"
        elif(media1 >= 5 and media1 < 7):
            final1 = "Recuperação"
        else:
            final1 = "Reprovado"
    
    elif(n == 1):
        media2 = (float(nota1) + float(nota2) + float(nota3)) / 3.0
        
        if(media2 >= 7):
            final2 = "Aprovado"
        elif(media2 >= 5 and media1 < 7):
            final2 = "Recuperação"
        else:
            final2 = "Reprovado"
    
    elif(n == 2):
        media3 = (float(nota1) + float(nota2) + float(nota3)) / 3.0
        
        if(media3 >= 7):
            final3 = "Aprovado"
        elif(media3 >= 5 and media1 < 7):
            final3 = "Recuperação"
        else:
            final3 = "Reprovado"


print(f"O aluno 1 teve média: {media1} , status: {round(final1, 2)}")
print(f"O aluno 2 teve média: {media2} , status: {round(final2, 2)}")
print(f"O aluno 3 teve média: {media3} , status: {round(final3, 2)}")
    
