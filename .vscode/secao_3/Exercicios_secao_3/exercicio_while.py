"""
Iterando strings com while
"""
nome = "Ricardo Silva"
indice = 0
novo_nome = ''
tamanha_nome = len(nome)

while indice < tamanha_nome:
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += "*"
print(novo_nome)



