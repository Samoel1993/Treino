#1)

num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
num3 = float(input("Digite o terceiro valor: "))

if(num1 > num2) and (num1 > num3):
    print("O maior valor é :" , num1)
elif(num2 > num1) and (num2 > num3):
    print("O maior valor é: ", num2)
elif(num3 > num1) and (num3 > num2):
    print("O maior valor é: ", num3)
    
#2)--------------------------------------------------------------------
primeiro = int(input('Primeiro numero: '))
segundo  = int(input('Segundo numero : '))
terceiro = int(input('Terceiro numero: '))

print(primeiro,'-',segundo,'-',terceiro)

if(terceiro > segundo):
        ordem = terceiro
        terceiro = segundo
        segundo = ordem

if(segundo > primeiro):
        ordem = segundo
        segundo = primeiro
        primeiro = ordem

if(terceiro > segundo):
        ordem = terceiro
        terceiro = segundo
        segundo = ordem

print(primeiro,'-',segundo,'-',terceiro)


#3)--------------------------------------------------------------------
jogador1 = int(input("Primeiro jogador digite: (0)- Pedra, (1)- Papel, (2)- Tesoura: "))
jogador2 = int(input("Segundo jogador digite:  (0)- Pedra, (1)- Papel, (2)- Tesoura: "))

pedra = 0
papel = 1
tesoura = 2

if(jogador1 == jogador2):
    print("Empate, Ninguem ganhou")
elif(jogador1 - jogador2 == 2) or (jogador1 - jogador2 == 1):
    print("Jogador 1 ganhou.")
else:
    print("Jogador 2 Ganhou.")
