Lista1 = [1,2,3,4,5]
Lista2 = [6,7,8,9,10]
Lista3 = [11,12,13,14,15]
todas_as_listas = [Lista1, Lista2, Lista3]
print(todas_as_listas)

produtos = ["TV", "celular", "mouse", "teclado", "tablet"]
print(produtos[1])

produtos2 = ['tv', 'celular', 'mouse', 'teclado', 'tablet']
vendas = [1000, 1500, 350, 270, 900] 
print("As vendas do ", produtos2[2], "foram de:", vendas[1])

produtos3 = ['tv', 'celular', 'mouse', 'teclado', 'tablet']
i = produtos3.index('mouse')
print("O valor d i é : " + str(i))
print("O produto de posição i é: "+ str(produtos3[i]))

produtos4 = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
estoque = [100,150,100,120,70,180,80]

produtos4 = input("Insira o nome do produto e letra minuscula: ")
i = produtos4.index(produtos4)
print(i)