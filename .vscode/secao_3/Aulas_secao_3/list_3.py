"""
Listas em Python
Tipo List - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adicuina um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update  Delete
Criar  Ler  Alterar Apagar = lista[1] (CRUD)
"""

#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Ricardo')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(1, 0)
print(lista)