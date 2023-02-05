a = "Luiz"
b = "querida"

concatenar = a + " "+ b
print(concatenar)


a = "Luiz"
b = "querida"

concatenar = a + " "+ b

tamanho = len(concatenar) # contar caracteres
print(tamanho)


#navegando pelo índice

a = "Luiz"
b = "querida"

concatenar = a + " "+ b

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])


# Imprimindo parte e uma string

a = "Luiz" # uma string / on=jeto de string
b = "querida"

concatenar = a + " "+ b

print(concatenar[0:5]) 


#ALterando a caixa: Minusculo

a = "Luiz"
b = "querida"

concatenar = a + " "+ b

print(concatenar)
print(concatenar.lower())
print(concatenar.upper())
print(concatenar)

#Aplicando um valor
a = "Luiz"
b = "querida"

concatenar = a + " "+ b
print(concatenar)
concatenar = concatenar.upper()
print(concatenar)


#Removendo espaço no começo  e no fim da string

a = "Luiz"
b = "querida"

concatenar = a + " "+ b + "\n" # \n quebra de linha

print(concatenar.strip())  # remove a quebra de linha e o ("espaço")

# converter uma string em uma lista

minha_string = " O luiz mé bonito demais e lindão"

minha_lista = minha_string.split(" ") 
print(minha_lista)

# Busca po substring

minha_string = " O luiz mé bonito demais e lindão"

busca = minha_string.find("rei")
print(busca)

#print(minha_string[busca:]) pegar parte da string


# substitui parte de uma string

minha_string = " O luiz mé bonito demais e lindão"

minha_string = minha_string.replace("rei", "rainha" )
print(minha_string)