# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
p1= {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    #'idade': 900,
}

# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# nome = p1.popitem()
# print(nome)
# print(p1)

# p1.update({
#     'nome' : 'Ricardo',
#     'idade' : 25
# })

# p1.update(nome= 'Ricardo', idade='25')

tupla = ('nome', 'Ricardo'), ('idade', 25), ('sobrenome', 'Silva')
lista = ['nome', 'Ricardo'], ['idade', 25], ['sobrenome', 'Silva']

p1.update(lista)

for chave, valor in p1.items():
    print(chave, valor)