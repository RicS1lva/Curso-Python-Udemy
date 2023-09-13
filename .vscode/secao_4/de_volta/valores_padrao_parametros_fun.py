def soma(x=None, y=None, z=None):
    if z is None:
        print(f'{x=} + {y=}', x + y)
    elif x is None:
        print(f'{y=} + {z=}', y + z)
    elif y is None:
        print(f'{x=} + {z=}', x + z)

    else:
        print(f'{x=} + {y=} + {z=}', x + y + z)

soma(x=1, y=2)
soma(y=3, z=4)
soma(x=5, z=7)
soma(5, 6, 8)

