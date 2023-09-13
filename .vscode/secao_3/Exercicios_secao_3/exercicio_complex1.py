"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

"""

numero = input("Digite um número inteiro: ")


if numero.isdigit():
    
    par_ou_impar = int(numero) % 2
    
    if par_ou_impar == 0:
        print("Este é um número Par!")
    else:
        print("Este é um número Ímpar!")

else:
    print("Este não é um número inteiro!")