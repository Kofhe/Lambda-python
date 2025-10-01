#gere uma lista contendo os antecessores de cada numero

numeros = [1,2,3]
antecessores = list(map(lambda x: x-1, numeros))

print(antecessores)
