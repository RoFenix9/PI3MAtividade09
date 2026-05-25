horas = int(input("Digite a quantidade de horas registradas: "))

contador = 1
total = 0

while contador <= horas:
    producao = int(input("Digite a produção da hora: "))
    total = total + producao
    contador += 1

media = total / horas

print("Produção total:", total)
print("Produção média por hora:", media)
