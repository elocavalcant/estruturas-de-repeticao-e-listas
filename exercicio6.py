aluno1 = [5,8,10,9]
aluno2 = [8,8,1,5]
aluno3 = [9,8,6,7]
aluno4 = [7.5,4,9,8]
aluno5 = [3,7,2,6]
aluno6 = [6,8,7.3,7.7]
aluno7 = [7,6,4,9.1]
aluno8 = [10,10,10,10]
aluno9 = [5,8,9,4]
aluno10 = [5,7,9,10]
alunos = [aluno1,aluno2,aluno3,aluno4,aluno5,aluno6,aluno7,aluno8,aluno9,aluno10]
contagem = 0
final = ""
media = 0
for i in alunos:
    for nota in alunos[contagem]:
        media = media + nota 
    media = media / len(alunos[contagem])
    if media >= 7:
            final = f"{final} Aluno {contagem+1} (Aprovado) - {media} |"
    contagem += 1
    media = 0
print("Médias:", final)