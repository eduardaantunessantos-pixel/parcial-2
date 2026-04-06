# cálculo de juros simples

print("Cálculo de Juros Simples")
print("Fórmula: J = (C * I * T) / 100")

# solicita os valores
C = float(input("Digite o capital (C): "))
I = float(input("Digite a taxa (I): "))
T = float(input("Digite o tempo (T): "))

# calcula os juros
J = (C * I * T) / 100

# mostra o resultado
print("O valor dos juros é:", J)