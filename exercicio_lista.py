"""def main():
    n = int(input("Digite o número de notas: "))
    notas = leNota(n)
    print("As notas são: ", notas)
    print("A media é: ", format(calculaNotas(notas), ".1f"))




def leNota(num):
    notas = []
    for i in range(1, num+1):
        dado = float(input(f"Digite a {i}° nota: "))
        notas.append(dado)
    return notas


def calculaNotas(notas):
    soma = 0
    for i in range(len(notas)):
        soma = soma + notas[i]
    return(soma/len(notas))


main()"""

"""def soma(numero1, numero2=5):
    return numero1 + numero2
print(soma(3, 10))


def posOuNeg(numero):
    if numero < 0:
        return "N"
    elif numero > 0:
        return "P"
    else:
        return "Z"
    
n = posOuNeg(0)
print(n)"""


"""def reverso(n):
    inverte = str(n)
    print(inverte[::-1])"""

def tamanhoNumero(x):
    return len(str(x))

num = int(input("Digite um numero: "))
print(tamanhoNumero(num))


def numeroPotencia(x):
    




