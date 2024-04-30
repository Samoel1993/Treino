#1--------------------------------------------
test1 = input("Informe o texto 1 : ")
test2 = input("Informe o texto 2: ")

posição = test1.find(test2)

if posição == -1:
    print(f"{test2} não encontrada em {test1}")
else:
    print(f"{test2} encontrada na posição {posição} de {test1}")
    
#2)-------------------------------------------------------
texto1 = input("Informe o texto 1: ")
texto2 = input("Informe o texto 2: ")

escolhidos = ""
for x in texto1:      
    if x in texto2 and x not in escolhidos:
        escolhidos += x

print(escolhidos)

#3-----------------------------------------

tex1 = input("Informe o texto 1: ")
tex2 = input("Informe o texto 2: ")
tex3 = input("Informe o texto 3: ")

caneta = ""

for x in tex1:
    if x in tex2 and x in tex3:
        caneta += x
print(caneta)


#4)-------------------------------

t1 = input("Informe 1°: ")
t2 = input("Informe 2°:")

t3 = ""

for x in t1:
    if x not in t2:
        t3 += x
print(t3) 
