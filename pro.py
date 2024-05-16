"""tabela = {
    "Alface": 0.45,
    "Batata": 1.2,
    "Tomate": 2.3
}
tabela ["Banana"] = 1
del tabela["Banana"]
    
for chave in tabela:
    print("Chave: ", chave, "Valor: ", tabela[chave])
    """
    
    
"""x = {'a':1, 'b':2, 'c':3}
y = {'z':9, 'b':7}
x.update(y)
x.update(a = 7, c = 'ceca', d=18)

print(x)"""


"""D2 = {'spam': 2, 'eggs': 3}
D3 = {'food': {'ham': 1, 'eggs': 2}}

print(D3['food'])
print(D3['food']['ham'])

D2.update(D3)
print("D2", D2)
print("D2 len", len(D2))
"""

"""x = {'joao': [1,2], 'maria': [3,4]}
y = x.copy()
y['josé'] = [2,6]
a = chave_removido, valor_removido = y.popitem()
print(y)
print(a)"""

#Guardando o valor na variavel
"""x = {'joao': [1,2], 'maria': [3,4]}
y = x.copy()
y['josé'] = [2,6]
a = valor_removido = y.pop('joao')
print(y)
print(a)"""


#Atualiza o dicionario com elementos de outros
"""x = {'a': 1, 'b':2, 'c':3}
y = {'z': 9, 'b': 7}
x.update(y)
print("Juntou o dicionario y com o dicionario x",x)
print("---------------------------------")
x.update(a=7, c='ceca', d=18)
print("Além de juntar ele atualiza e adiciona elementos no dicionario",x)"""

#Aninhamento
"""D2 = {'spam': 2, 'eggs': 3}
D3 = {'food': {'ham': 1, 'eggs':2}}
print(D3)
print("Ele acessa o valor do dicionario dentro do dicionario",D3['food']['ham'])

print("-------------------------------------------------------------")
D2.update(D3)
print(D2)
print("ele vai percorrer o dicionario com len:", len(D2))

print('---------------------------')
del D2['eggs']
print('Del excluiu a chave e o valor do eggs que tava no dicionario D2',D2)"""

#Registro de dados
"""bob = {"name": 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'mus'}
tom = {'name': 'Tom', 'age': 50, 'pay': 0, 'job': None}

#database
db = {}
db['Bob'] = bob
db['Sue'] = sue
db['Tom'] = tom

print(db)"""


#Matrix

"""Matrix = {}

Matrix[(2,3)] = 88
Matrix[(7,8)] = 99
print(Matrix)"""


#Matrizes com Dicionarios

"""m1 = {}
i, j = 4, 3

for a in range(1,i):
    for b in range(1,j):
        m1[(a,b)] = 0
        
print(m1)"""


#soma de duas matrizes
"""m1 = {}
m2 = {}
mRes = {}
i, j = 2, 2
l, k = 2, 2
m1[(0,0)] = 1
m1[(0,1)] = 3
m1[(1,0)] = 2
m1[(1,1)] = 0

m2[(0,0)] = 1
m2[(0,1)] = 3
m2[(1,0)] = 2
m2[(1,1)] = 0

for a in range(0,i):
    for b in range(0,j):
        mRes[(a,b)] = m1[(a,b)] + m2[(a,b)]
print(mRes)"""