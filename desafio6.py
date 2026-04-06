# programa para converter tempo

print("1 - Converter segundos para horas, minutos e segundos")
print("2 - Converter horas, minutos e segundos para segundos")

opcao = int(input("Digite a opção: "))

if opcao == 1:
    # recebe segundos
    segundos = int(input("Digite o número de segundos: "))

    # conversão
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    seg = segundos % 60

    # resultado
    print(horas, "hora(s)", minutos, "minuto(s)", seg, "segundo(s)")

elif opcao == 2:
    # recebe horas, minutos e segundos
    horas = int(input("Digite as horas: "))
    minutos = int(input("Digite os minutos: "))
    segundos = int(input("Digite os segundos: "))

    # conversão para segundos
    total = horas * 3600 + minutos * 60 + segundos

    # resultado
    print("Total em segundos:", total)

else:
    print("Opção inválida")