def calculos_simples(numero1, numero2):
    soma = numero1 + numero2
    sub = numero1 - numero2
    multi = numero1 * numero2
    div = numero1 / numero2
    return soma, sub, multi, div

def regra_de_tres(number1, number2, number3):
    regra_proporcional = (number2 * number3) / number1 
    regra_inversa = (number1 * number2) / number3
    return regra_proporcional, regra_inversa



while True:
    calculo = input("Informe o calculo que deseja realizar: (Cal)-Calculo simples ou (Regra)-Regra de 3: ")
    if calculo.lower() == "cal":
        valor1 = float(input("Digite um numero: "))
        valor2 = float(input("Digite outro numero: "))
        operacao = input("Informe a operação que deseja realizar: soma(+), subtração(-), multiplicação(*) ou divisão(/): ")
        resultado = calculos_simples(valor1, valor2)
        if operacao == "+" or operacao == "soma":
         print(f"O total da soma é de: {resultado[0]}")
        elif operacao == "-" or operacao == "subtracao":
        
            print(f"O total da subtração é de: {resultado[1]}")
        
        elif operacao == "*" or operacao == "multiplicação":
            print(f"O total da subtração é de: {resultado[2]}")
        
        elif operacao == "/" or operacao == "divisão":
            print(f"O total da subtração é de: {resultado[3]}")
        else:
         print("operação invalida")

        continua = input("Deseja continuar? digite sim ou não: ")
        if continua == "não":
            break
        else:
            continue
        
    if calculo.lower() == "regra":
        valor1_regra = float(input("Digite o primeiro numero: "))
        valor2_regra = float(input("Digite o segundo numero: "))
        valor3_regra = float(input("Digite o terceiro numero: "))
        operacao_regra = input("Informe se a regra de 3 proporcional ou inversamente proporcional: (propor)- Proporcional, (inversa)- inversamente proporcional: ")
        if operacao_regra.lower() == "propor":
            resultado_regra_propor = regra_de_tres(valor1_regra, valor2_regra, valor3_regra)
            print(f"O resultado da regra de 3 proporcional é: {resultado_regra_propor[0]} ")
        elif operacao_regra.lower() == "inversa":
            resultado_regra_inversa = regra_de_tres(valor1_regra, valor2_regra, valor3_regra)
            print(f"O resultado da regra de 3 inversamente-proporcional é: {resultado_regra_inversa[1]}")
        else:
            print("Regra invalida.")
            
        continua = input("Deseja continuar? digite sim ou não: ")
        if continua == "não":
            break
        else:
            continue
            