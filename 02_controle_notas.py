nome = input("Digite seu nome: ")
nota = 0.0
soma = 0.0
nota2 = "sim"
quantidade = 0.0

while nota2.lower() == "sim":
    nota = float(input("Digite a nota: "))
    soma = soma + nota
    quantidade = quantidade + 1
    nota2 = input("Deseja digitar outra nota?: ")

media = soma / quantidade
print (f"Sua média é {media}")


