#1)===================================================================

"""lista = []
num = int(input("Informe um numero: "))

for i in range(1, num+1):
    numero = int(input(f"Digite o {i}° numero: "))
    lista.append(numero)

print(lista)"""

#2)=================================================================

"""array = []

number = int(input("Digite a quantidade de numeros: "))

for i in range(1, number+1):
    numero = float(input(f"Digite o {i}° numero: "))
    array.append(numero)
    
print(array[::-1])"""


#3)======================================================================

"""lista_notas = []

for i in range(4):
    notas = float(input(f"Informe a {i+1}° nota: "))
    lista_notas.append(notas)

media = sum(lista_notas) / len(lista_notas)
print("As notas do aluno: ", lista_notas)
print("A média do aluno é: ", media)"""


#4)================================================================

"""lista_caracteres =[]

for x in range(10):
    caracteres = str(input(f"Informe o {x+1}° caractere: "))
    lista_caracteres.append(caracteres)

for x in lista_caracteres:    
    if x not in ["a", "e", "i", "o", "u"]:
        print(x)"""
        
        
#5)======================================================================================

"""par = []
impar = []
total = []

for s in range(20):
    numero = int(input(f"Informe o {s+1}° numero: "))
    total.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
        
print("Total: ", total)
print("Par: ", par)
print("Impar: ", impar)"""


#6)Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene
#num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0

"""
media_aluno = []

for s in range(5):
    print(f"Informe as notas do {s+1}° aluno: ")
    notas = []
    for s in range(4):
        nota = float(input(f"Informe a {s+1}° nota: "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    media_aluno.append(media) 


t = 0
for s in media_aluno:
    if s >= 7.0:
        t += 1
print(f"O numero de alunos que foram aprovados é: {t}")
"""

# 7) Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.


"""lista_numero_soma = []
lista_numero_multi = []

for j in range(5):
    numero = int(input(f"Informe o {j+1}° numero: "))
    lista_numero_soma.append(numero + numero)
    lista_numero_multi.append(numero * numero)
    
  
    
print("A multiplicação: ", lista_numero_multi)
print("A soma: ", lista_numero_soma)
"""

#8) Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida

"""idade = []
altura = []

for u in range(5):
    idade_pessoa = int(input(f"Informe a  idade da {u+1}° pessoa: "))
    altura_pessoa = float(input(f"Informe a altura da {u+1}° pessoa: "))
    idade.append(idade_pessoa)
    altura.append(altura_pessoa)
print(f"A idade na ordem lida:{idade} / idade na ordem inversa: {idade[::-1]}")
print(f"A altura na ordem lida: {altura} / altura na ordem inversa: {altura[::-1]}")"""

#9)Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor

"""a = []

for i in range(10):
    numero = int(input(f"Informe o {i+1}° numero: "))
    a.append(numero** 2)
    
print(a)"""


#10) Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos 
# intercalados dos dois outros vetores.

"""array1 = []
array2 = []

for a in range(10):
    numero1 = int(input(f"Array 1: Informe o {a+1}° numero: "))
    numero2 = int(input(f"Array 2: Informe o {a+1}° numero: "))
    array1.append(numero1)
    array2.append(numero2)
array3 = array1 + array2
array3.sort()

print("Array 1:",array1)
print("Array 2",array2)
print("Array 3",array3)"""


#
    


        
        
