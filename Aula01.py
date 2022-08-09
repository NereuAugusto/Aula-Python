print(2+3)
print(4-7)
print(2*5.3)
print(9.4/3)
print(10%3)
#potencia 
print(2**5.3)
#pega o numero que foi usado pra dividir 
print(10//3)
#raiz
print(81 ** (1/2))
#vazio é diferente de nulo que é diferente de 0

#tipo String 
dir(str)

nome = 'Andre Insardi'
print(nome)

print('Andre' == "Andre")
texto = 'texto entre apostrófos pode ter "aspas"'
print(texto)

doc= """texto com multiplas linhas..."""
print(doc)

#pegar letras especificas de um texto
nome = "Um nome qualquer"
nome[0]
nome[6]
nome[-3]
print(nome[-3])
#n conta os 4 primeiros 
nome[4:]
print(nome[4:])
#n pega os ultimos 5
print(nome[-5:])
#vai pegar até o caracter 4, no entando ele n pega o ultimo elemento, é o intervalo de valores, rpimeiro pega mas o ultimo n 
print(nome[:4])
#pega um intervalo de valores
print(nome[2:5])
#pega tudo 
numero = '123456789'
print(numero[::])
#pula numeros
print(numero[::2])
#inverter uma string 
print(numero[::-1])
#pula os 3 primeiros e depois vai de dois em dois 
print(numero[3::2])