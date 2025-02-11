#Transforma apenas a primeira letra de uma string em maiuscula

nome = "mateus"

print(nome.capitalize() , "\n")

#Transforma todas as letras em minusculas
nome = "mateus"

print(nome.casefold() , "\n")

#CONTA O NUMERO DE VEZES QUE UM CARACTERE ESPECIFICO APARECE NA STRING.

nome = "mateusdecamposturkoco@gmail.com"
print(nome.count ('a') , "\n")

#RETORNA true (verdadeiro) OU false (falso) PARA UM TESTE se A STRING TERMINA COM UMA STRING ESPECIFICA

nome = "mateusdecamposturkoco@gmail.com"
print(nome.endswith ('gmail.com'), "\n")

#ENCONTRA A POSIÇÃO DO TERMO PROCURADO, LEMBRE-SE COMEÇA DO ZERO
nome = "mateusdecamposturkoco@gmail.com"
print(nome.find ('@') , "\n")

#VERIFICA SE O TEXTO É todo FEITO COM LETRAS

nome = "mateus"

print(nome.isalpha() , "\n")

#VERIFICA SE O TEXTO É FEITO COM NUMEROS.

nome = "123"
print(nome.isnumeric() , "\n")

#SUBSTITUI UM CARACTERE ESCOLHIDO POR OUTRO.
nome = "Mateus"
print(nome.replace ('o', 'u'), "\n")

#SEPARA O TEXTO STRING EM BASEADO EM ALGUM CARACTERE INDICADO 
nome = "mateus @ decampos turkoco"
print(nome.split ('@') , "\n")

#COLOCA TODAS AS LETRAS INICIAIS EM MAIUSCULA.
nome = "mateus de campos turkoco"
print(nome.title() , "\n")

#RETIRA OS CARACTERES INDESEJADOS, COMO POR EXEMPLO ESPAÇOS QUE NAO AGREGAM VALOR.
nome = " mateus de campos turkoco "
print(nome.strip() , "\n")

#RETORNA TRUE OU FALSE PARA UM TESTE DE UMA STRING SE INICIA COM UMA TEXTO ESPECIFICO.
nome = "mateus 2008"
print(nome.startswith("ser") , "\n")
print(nome.startswith("Ser") , "\n")
