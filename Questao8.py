inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))

while inicio <= fim:
    if inicio % 2 == 0:
        print(inicio)
    
    inicio += 1
