estoque = [1,2,3,4,5,6,7,8,9,10,11,12,13]
produtos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
nivel_minimo = 50
for i, qtde in enumerate(estoque):
    if qtde < nivel_minimo:
            print(produtos [i] ,qtde)