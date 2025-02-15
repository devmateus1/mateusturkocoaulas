nomes = ['mateus', 'jose', 'joao', 'guilherme','jorge']
bairro = ['panagua', 'vila nova', 'sao paulo', 'rio de janeiro', 'bahia']
telefone = [121212, 131313, 141414, 151515, 161616]
pesquisa = input("Digite o nome do usuario : ")
if pesquisa in nomes:
    i = nomes.index(pesquisa)
    nomecliente = nomes[i]
    bairrocliente = bairro[i]
    telefonecliente = telefone[i]
    print("O cliente {} do bairro {} com telefone {} foi cadastrado".format(nomecliente, bairrocliente, telefonecliente))
else:
    print("Cliente não encontrado")