import random
import sys



for _ in range(10):
    
    cpf = ''
    for i in range(9):
        cpf += str(random.randint(0, 9))


    nove_digitos = cpf[ :9]
    contador_regressivo_1 = 10

    resultado_digt_1 = 0
    for digit_1 in nove_digitos:
        resultado_digt_1 += int(digit_1) * contador_regressivo_1
        contador_regressivo_1 -= 1

    digit_1 = (resultado_digt_1 * 10) % 11
    digit_1 = digit_1 if digit_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digit_1)
    contador_regressivo_2 = 11

    resultado_digit_2 = 0
    for digit_2 in dez_digitos:
        resultado_digit_2 += int(digit_2) * contador_regressivo_2
        contador_regressivo_2 -= 1

    digit_2 = (resultado_digit_2 * 10) % 11
    digit_2 = digit_2 if digit_2 <= 9 else 0

    cpf_valido = f'{nove_digitos}{digit_1}{digit_2}'

    print(cpf_valido)
