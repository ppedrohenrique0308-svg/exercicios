ni = input('escreva uma palavra: ')
dicionario = {}
for letra in ni:
    if letra in dicionario:
        dicionario[letra] += 1
    else:
        dicionario[letra] = 1
print(dicionario)