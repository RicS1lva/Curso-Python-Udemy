"""
Exercícios
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro
"""

# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 4

# q = quadruplicar
# d = duplicar
# t = triplicar

# print(d(2), t(2), q(2))

def create_multi(multi):
    def multiply(number):
        return number * multi
    return multiply

double = create_multi(2)
triple = create_multi(3)
quad = create_multi(4)

print(double(4))
print(triple(4))
print(quad(4))
