# Calculadora simples em Python

# Pede pro usuário digitar o primeiro número
num1 = float(input("Digite o primeiro número: "))

# Pede pro usuário digitar o segundo número
num2 = float(input("Digite o segundo número: "))

# Mostra as opções de operação pro usuário escolher
print("Escolha a operação:")
print("1 - Adição (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

# Pede pra pessoa escolher qual operação quer fazer
operacao = input("Digite o número da operação (1/2/3/4): ")

# Aqui a gente vai ver qual operação a pessoa escolheu e calcular
if operacao == "1":
    resultado = num1 + num2  # soma os dois números
    simbolo = "+"
elif operacao == "2":
    resultado = num1 - num2  # subtrai o segundo do primeiro
    simbolo = "-"
elif operacao == "3":
    resultado = num1 * num2  # multiplica os dois
    simbolo = "*"
elif operacao == "4":
    if num2 != 0:  # se não for divisão por zero
        resultado = num1 / num2
        simbolo = "/"
    else:
        resultado = "Erro! Não dá pra dividir por zero 😅"
        simbolo = "/"
else:
    resultado = "Ops! Operação inválida"
    simbolo = ""

# Mostra o resultado bonitinho pro usuário
print(f"\nResultado: {num1} {simbolo} {num2} = {resultado}")