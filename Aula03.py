#Loop

#While
from random import randint


a = 10
while a > 0: 
    print(a)
    a = a - 1


#For
#x é o contador // range 
for x in range(1,11):
    for y in range(1,11):
        print(x * y)

#For
#formatado
for x in range(1,11):
    for y in range(1,11):
        #Chave busca o valor e apresenta ele, e o F indica que é uma formatação 
        print(f'{x} * {y} = {x * y}')

#Lista de dias da semana 
dias_semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']

for dia in dias_semana:
    print(f'Hoje é {dia}')

lista_pessoas = [{'id': 1, 'nome': 'Andre', 'idade': 30, 'altura': 1.83, 'cursos':['c#', 'Python', 'Node']},
                {'id': 2, 'nome': 'Juzao', 'idade': 62, 'altura': 1.50, 'cursos':['c#', 'Python', 'c++']},
                {'id': 3, 'nome': 'Lulu', 'idade': 5, 'altura': 1.51, 'cursos':['Python', 'Node']},
                {'id': 4, 'nome': 'Joquita', 'idade': 5, 'altura': 1.92, 'cursos':['c#', 'Java', 'React']}]

for pessoa in lista_pessoas:
    for curso in pessoa['cursos']:
        nome = pessoa['nome']
        print(f'A pessoa {nome} faz o curso {curso}')

#Lista pessoas é uma lista, pessoa é um dicionario e curso é uma lista 


#Exercicio 1

nome = 'Nereu'
print(nome[::-1])

frase = 'Python é uma linguagem excelente'

#for pessoa in range(1,32):
 #   for y in range(1,11)


#3

salario = 3450.45
despesas = 2456.2
#Caule o percentual do salário comprome6do com as despesas

sal_comp = (despesas/salario)*100
print(sal_comp)

#4

x = int(input('Valor de X: ')) 
y = int(input('Valor de y: '))

resultado = (f'A soma de {x} com {y} é {x + y}')
print(resultado)

#5

idade = int(input('A idade da pessoa é: '))

if idade < 18: 
    print('Menor de idade')
elif 18 <= idade <= 65:
    print('Aulto') 
elif 66 <= idade <= 100:
   print('Melhor idade')
else:
    print('Centenário ')


#6

nome = "paralelepípedo"
for letra in nome:
    print(f'{letra},', end="")


#7

nome = ('Danieli', 'André', 'Marcelo', 'Ana Paula')
for nomenclatura in nome:
    print(nomenclatura)


sorteio = randint(0,9)

valor = int(input('Insira um número de 0 a 9: '))
if valor == sorteio:
    print("Número secreto x foi encontrado!")
else: print('Errou vaca!')