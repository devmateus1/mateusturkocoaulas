#Faça um programa que receba uma nota do aluno e se for superior ou igual a 7 apareça mensagem, ele esta aprovado, se for inferior a 5 ele esta "reprovado" e se estiver entre 5 e 7
#apareça a mensagem"recuperação"
nota = int(input("Qual foi sua nota: "))
if nota >= 7:
    print("Você esta aprovado")
elif nota < 5:
    print("Você esta reprovado")
else:
    print("Voce esta em recuperação")


if nota >= 7:
    print("Você esta aprovado")
else:
    if nota <= 5:
        print("Recuperação")
    else:
        print("Reprovado")