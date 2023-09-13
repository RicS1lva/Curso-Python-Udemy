"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor
"""

def soma(x, y):

    print(f'{x=} {y=}' '|' 'x + y =', x + y)

soma(4, 5)
soma(5, 4)
soma(y=5, x=4)
