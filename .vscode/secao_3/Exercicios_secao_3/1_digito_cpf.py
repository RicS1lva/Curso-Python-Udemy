"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)
import re
import sys

# cpf_enviado_usuario = '746.824.890-70' \
#     .replace('.', '') \
#     .replace(' ', '') \
#     .replace('-', '')
entrada = input('Digite seu CPF: ')
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

nove_digitos = cpf_enviado_usuario[ :9]
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

cpf_gerado = f'{nove_digitos}{digit_1}{digit_2}'

if cpf_gerado == cpf_enviado_usuario:
    print("CPF VÁLIDO")
else:
    print('CPF inválido')
