"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

"""

nome_usuario = input("Digite seu primeiro nome: ")
quantidade_letras = len(nome_usuario)
curto = quantidade_letras <= 4
normal = quantidade_letras >= 5 and quantidade_letras <=6

if curto:
    print("Seu nome é curto!")
elif normal:
    print("Seu nome é normal!")
else:
    print("Seu nome é muito grande!")    