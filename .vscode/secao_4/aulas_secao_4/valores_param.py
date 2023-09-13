"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetro podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar seu código.
"""

def soma(x, y=7, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}',x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(1, 2)
soma(3, 4)
soma(5, 6)
soma(1)
soma(1, 6, 7)