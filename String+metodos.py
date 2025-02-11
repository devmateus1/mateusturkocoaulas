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
print(nome.enswith ('gmail.com') , "\n")