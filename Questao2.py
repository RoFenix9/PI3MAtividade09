n = int(input("Digite um número inteiro positivo: "))

contador = 1
soma = 0

while contador <= n:
    soma = soma + contador
    contador += 1

print("A soma é:", soma)
