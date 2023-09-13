"""
Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo
par de "chave" e "valor"
Chaves podem ser consideradas como o "índice"
que vimos na lista e podem ser de tipo imutáveis
como: str, int, bool, float, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro
dicionário.
Usamos as chaves - {} - ou a classe dict para criar
dicionários.
Imutáveis: str, int, floar, bool, tuple
Mutável: dict, list
"""
pessoa = {
    'nome': 'Ricardo',
    'sobrenome': 'Silva',
    'idade': '25',
    'altura': 1.83,
    'enderecos': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'ota ota', 'numero': 456}
    ]}

for chave in pessoa:
    print(chave, pessoa[chave])