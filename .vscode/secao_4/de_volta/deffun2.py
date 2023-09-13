def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é multiplo de {multiplo}?', end=' R:')
    print(resultado)


multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)
