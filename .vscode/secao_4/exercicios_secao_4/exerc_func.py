"""
Exercícios com funções

Crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variável e mostre o valor
da variável."""

def multiply(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multi = multiply(20, 30, 54, 56, 98)
print(multi)
print(20*30*54*56*98)

"""
Crie uma função que fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar.
"""
def impar_par(number):
    impar = number % 2 == 0
    if impar:
        return "Par"
    return "Impar"

print(impar_par(54))
print(impar_par(45))
print(impar_par(10))

# numero_1 = input('Digite um número: ')
# numero_2 = input('Digite outro número: ')

# def soma(*args):
#     multi = 1
#     for numero in args:
#         multi = (multi * int(numero))

#     return multi

# print(soma(numero_1, numero_2))

# numero = input('Digite um número: ')

# def impar_par(x):
#     par_impar = x % 2
#     if par_impar == 0:
#         print("Este é um número par")
#     else:
#         print("Este é um número ímpar")

# impar_par(int(numero))
