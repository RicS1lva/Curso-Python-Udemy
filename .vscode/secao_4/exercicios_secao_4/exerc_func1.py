# #Exercícios com funções

# #Crie uma função que multiplique todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multi_1 = multiplica(2, 3)
print(multi_1)

multi_2 = multiplica(1, 2, 3, 4)
print(multi_2)

multi_3 = multiplica(22, 3, 100, 5)
print(multi_3)


# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar

def par_impar(x):
    if x % 2 >= 1:
        return f'O número {x} é ímpar'
    return f'O número {x} é par'


par_impar1 = par_impar(2)
print(par_impar1)

par_impar2 = par_impar(5)
print(par_impar2)

par_impar3 = par_impar(24)
print(par_impar3)


