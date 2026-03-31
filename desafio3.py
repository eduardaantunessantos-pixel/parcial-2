# Programa para criar uma lista de 5 nomes e imprimir todos

# Passo 1: Criar uma lista com 5 nomes
nomes = ["Ana", "Vanessa", "Gabriela", "Pietra", "Helena"]

# Passo 2: Imprimir cada nome da lista usando um loop for
print("Lista de nomes:")
for nome in nomes:
    print(nome)

# Passo 3: Permitir que o usuário adicione um novo nome à lista
novo_nome = input("Digite um novo nome para adicionar à lista: ")  # comando para o usuário responder
nomes.append(novo_nome)  # adiciona o nome digitado pelo usuário à lista

# Passo 4: Imprimir a lista atualizada
print("\nLista atualizada de nomes:")
for nome in nomes:
    print(nome)