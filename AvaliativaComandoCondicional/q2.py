nota_und1=float(input("Digite a sua nota da primeira unidade: "))
nota_und2=float(input("Digite a sua nota da segunda unidade: "))

media_disciplina = ((2*nota_und1+3*nota_und2)/5)

if media_disciplina < 20:
    print("Sua media nessa disciplina foi de: ",media_disciplina,", Você foi reporvado.")
elif media_disciplina >= 60:
    print("Sua media nessa disciplina foi de: ",media_disciplina,", Parabéns você foi aporvado.")
elif media_disciplina >= 20 and media_disciplina < 60:
    print("Sua media nessa disciplina foi de: ",media_disciplina,". Você realizará a prova final.")
    nota_prova_final = float(input("Digite a sua nota da prova final: "))
    media_final1 = (media_disciplina + nota_prova_final)/2
    media_final2 = ((2*nota_prova_final) +(3*nota_und2))/5
    media_final3 = ((2*nota_und1)+(3*nota_prova_final))/5
    if  media_final1 >= 60 and media_final1 >= media_final2 and media_final1>= media_final3:
        print("Sua média nessa disciplina é de", media_final1,". Parabéns, você foi aprovado.")
    elif media_final2 >= 60 and media_final2 >= media_final1 and media_final2 >= media_final3:
        print("Sua média nessa disciplina é de", media_final2,". Parabéns, você foi aprovado.")
    elif media_final3 >= 60 and media_final3 >= media_final1 and media_final3 >= media_final2:
        print("Sua média nessa disciplina é de", media_final3,". Parabéns, você foi aprovado.")
    else:
        print("Sua media nessa disciplina foi de: ",media_disciplina,", Você foi reporvado.")