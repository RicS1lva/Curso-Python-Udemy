"""
Listas em Python
Tipo list - Mutável
Suporta valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update  Delete
Criar  Ler  Alterar Apagar = lista[i] (CRUD)

interessante trabahar alterando o fim da lista, 
para não foder o processamento
"""
lista = [10, 20,  30, 40]
# lista[2] = 300
# del lista[2] # deleta itens selecionados da lista
# print(lista)
# print(lista[2])
# print(lista[2])

lista.append(50) #adiciona um elemento ao final da lista
lista.pop() #remove o elemento selecionado da lista(sem nada pega o ultimo)
lista.append(60)
lista.append(70)
lista.pop()
ultimo_valor = lista.pop() #o pop retorna sempre o valor removido
print(lista)


