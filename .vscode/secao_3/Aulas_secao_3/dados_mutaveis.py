"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ["Ricardo", 1, 4.5, 600]
lista_b = lista_a
lista_c = lista_a.copy()

lista_a.append('eita')
lista_a.insert(0, 'nossa')

print(lista_a)
print(lista_b)
print(lista_c)
