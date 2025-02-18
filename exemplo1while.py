venda = input("Registre o produto. Para cancelar o registro de um novo produto, basta apertar enter sem digitar nada: ")
vendas = []
while venda != '':
    vendas.append(venda)
    venda = input("Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter sem digitar nada: ")
print("Registros finalizados. As vendas cadastrados foram: {}".format (vendas))   