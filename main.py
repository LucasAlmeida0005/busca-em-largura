arestas = [
    [1],  # 0
    [0, 2],  # 1
    [1, 3, 4],  # 2
    [2, 4, 5],  # 3
    [2, 3, 5],  # 4
    [3, 4, 6],  # 5
    [5, 7, 8],  # 6
    [6],  # 7
    [6],  # 8

]

# inicio
inicial = 6

# vetores auxiliares
visitados = []
fila = []

for i in range(len(arestas)):
    visitados = [False] * len(arestas)
    # visitados[i] = False

print("Qtd Arestas:", len(arestas))

# fila.insert(1,inicial)
fila.append(inicial)
visitados[inicial] = 0

while len(fila) > 0:
    verticeAtual = fila[0]
    print("Atual: ", verticeAtual, '\n')
    for i in range(len(arestas[verticeAtual])):
        vizinho = arestas[verticeAtual][i]
        if visitados[vizinho] is False:
            # fila.insert(i, vizinho)
            fila.append(vizinho)
            # substituimos o fila.append(vizinho)
            visitados[vizinho] = visitados[verticeAtual] + 1
    fila.pop(0)

    print("Fila: ")
    x = 1
    for x in range(len(fila)):
        print(fila[x], " | ")
    print("\n")

print('Resultado: ')
for i in range(len(visitados)):
    print("[", i, "] -> ", visitados[i])




