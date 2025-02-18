pessoaspresentes = ['John Stones', 'Jesse Pinkman', 'Aria Stark', 'Tyrion Lannister']
chamada = 'Aria Stark'
for pessoa in pessoaspresentes:
    if pessoa == chamada:
        print('{} está presente.'.format (chamada))
        break
    else:
        print('Só um print para mostrar que o for passou por essa pessoa: '+str (pessoa))