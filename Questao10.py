orcamento = float(input("Digite o orçamento máximo: "))

total_gasto = 0
gasto = 0

while total_gasto <= orcamento:
    gasto = float(input("Digite um gasto: "))

    if gasto < 0:
        break

    total_gasto = total_gasto + gasto

    if total_gasto > orcamento:
        print("Orçamento excedido")
        break

sobrou = orcamento - total_gasto

print("Total gasto:", total_gasto)
print("Valor restante do orçamento:", sobrou)
