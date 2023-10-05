maior_altura = float("-inf")
menor_altura = float("inf")
soma_altura_homens = 0
qtd_mulheres = 0


for contador in range(16):
    altura = float(input("Digite a sua altura: "))
    genero = input("Digite o seu gênero: ").upper()

    if altura > maior_altura:
        maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura

    if genero == "M":
        soma_altura_homens += altura
    elif genero == "F":
        qtd_mulheres += 1


media_altura_homens = soma_altura_homens / (15 - qtd_mulheres)


print("Maior altura: ", maior_altura)
print("Menor altura: ", menor_altura)
print("Média da altura dos homens: ", media_altura_homens)
print("Quantidade de mulheres: ", qtd_mulheres)
