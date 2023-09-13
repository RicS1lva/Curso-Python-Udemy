'''
def soma(*args):
    total = 0
    for numero in args:
        print(f'{total} + {numero} =', total + numero)
        total += numero

soma(1, 2, 3, 4)

'''
def soma(*args):
    total = 0
    for numero in args:
        total += numero

    return total

soma1 = soma(1, 2, 3, 4)
print(soma1)
print(sum(1, 2, 3, 4))