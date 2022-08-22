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

#Listas [] vazio é uma lista
lista = []
print(type(lista))

len(lista)

lista.append(1)
lista.append(5)
lista[0]
print(lista)
print(len(lista))
#Aqui vc inseriu uma lista dentro de outra 
nova_lista = [1,5, 'Ana', 'Bia', ['C#', 'Python', 'Node'], 3.14]
print(nova_lista[3])
#Entra dentro da lista que está na lista, na posição 1
nova_lista[4][1]
print(nova_lista[4][1])
#Aqui vc entra dentro da lista dentro da lista e dentro do elemento 1 dessa lista, na posição 3
nova_lista[4][1][3]

#Remover elementos
print(nova_lista)
nova_lista.remove(5)
print(nova_lista)
#Inverte a lista toda 
nova_lista.reverse()
print(nova_lista)
#ou del
del nova_lista[2]
print(nova_lista)

#imprimir a posição do elemento especifico
lista = [1, 5, 'Raquel', 'Guilherme', 3.1415, 'Guilherme']
print(lista.index(5))
print(lista.index('Raquel'))
print(lista.index('Guilherme'))
#Procura o elemento especifico
'Andre' in lista
'Raquel' in lista
#Adicionar elemento no final da lista 
lista.append('Andre')
print(lista)
#inserir elemento na lista (posição/o elemento )
lista.insert(2, 'Ana')
print(lista)
lista.insert(2, ['Metalica', 'led', 'ozy'])

#De um a tres mas o 3 é aberto 
lista = ['Ana', 'Aline', 'Guilherme', 'Andre', 'Dani']
print(lista[1:3])
#isso imprime ['Aline', 'Guilherme']

print(lista[1:-1])
#isso imprime ['Aline', 'Guilherme', 'Andre']
print(lista[1:])
#isso imprime ['Aline', 'Guilherme', 'Andre', 'Dani']

#Tupla tem duas funções, é igual uma lista, é tipada dinamicamente, ms vc só consegue ver elemento e contar quantos existem
#vc não pode remover nem inserir nada 
tupla = ()
print(type[tupla])

cores = ('verde', 'amarelo', 'azul', 'branco')
cores[0]
cores[-1]
cores[1:]
print(cores)

#converter tupla em lista 
cores_list = list(cores)
print(cores)
print(cores_list)

#Dicionario -> estrutura chave vlaor 
#Se usa {} para dicionario 
pessoa = {}
type(pessoa)
#Tudo se organiza em tag e o conteudo, ou seja, andre está dentro de nome
pessoa = {'nome' : 'Andre', 'idade' : 35, 'altura' : 1.83}
pessoa 
pessoa['idade']
pessoa['nome']

pessoa = {'nome' : 'Andre', 'idade' : 35, 'altura' : 1.83, 'cursos': ['C#', 'Node', 'React', 'Python']}
pessoa
pessoa['altura']
pessoa['cursos']
pessoa['cursos'][2]

#Porcuro as chave, ou seja, nome, idade 
print(pessoa.keys())
#Procura valores como andre, 35
print(pessoa.values())
print(pessoa.items())
items = list(pessoa.items())

print(type(items))
print(items[3])
print(type(items[3]))
print(items[3][0])
print(type(items[3][0]))
print(items[3][1])
print(type(items[3][1]))
print(items[3][1][2])
print(type(items[3][1][2]))
print(items[3][1][2][4])
print(type(items[3][1][2][4]))




lista_pessoas = [{'nome' : 'Andre', 'idade' : 35, 'altura' : 1.83},
                 {'nome' : 'Ana', 'idade' : 22, 'altura' : 1.57},
                 {'nome' : 'João', 'idade' : 39, 'altura' : 1.78},
                 {'nome' : 'Bia', 'idade' : 27, 'altura' : 1.63}]

lista_pessoas[2]['idade']
pessoa1 = {'nome' : 'Andre', 'idade' : 35, 'altura' : 1.83}

pessoa1.update({'idade': 34, 'genero' : 'M'})
pessoa1


#Estrutura de condição IF

a = int(input('Digite o valor: '))
#print(a)
#type(a)

b = int(input('Digite o valor: '))
c = int(input('Digite o valor: '))

#se a > b E a > c então 
#resultado = a
#se não, se b > a E b > c entre 
#resultado = b
#se não
#resultado = c


resultado = 0 

if a > b and a > c: 
    resultado = a
elif b > c and b > a:
    resultado = b 
else:
    resultado = c

print(resultado)



