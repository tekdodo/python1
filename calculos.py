c = [6743, 253, 458, 2356]
g = [23248, 1834, 174]

# Função para somar elementos usando while
def somatorio(lista):
    soma = 0
    i = 0
    while i < len(lista):
        soma += lista[i]

        i += 1 #Ele adiciona o valor à direita (valor) ao valor atual da variável à esquerda (variavel) e, em seguida, atribui o resultado de volta para a mesma variável.
    return soma

# Cálculo da diferença
d = somatorio(g) - somatorio(c)

# Impressão dos resultados
print(f"Custos: R${somatorio(c)}")
print(f"Ganhos: R${somatorio(g)}")
print(f"Diferença: R${d}")
