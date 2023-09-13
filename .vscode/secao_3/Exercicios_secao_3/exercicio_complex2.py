"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

"""
hora_usuario = input("Que horas são?! ")
if hora_usuario.isdigit():

    hora = int(hora_usuario)
    bom_dia = hora >= 0 and hora <= 11
    boa_tarde = hora >= 12 and hora <= 17
    boa_noite = hora >= 18 and hora <= 23
    
    if bom_dia:
        print("Bom dia!")
    elif boa_tarde:
        print("Boa tarde!")
    elif boa_noite:
        print("Boa noite!")
    else:
        print("Desculpe, use apenas números entre 0 e 23!")

else:
    print("Por favor, use apenas números inteiros, entre 0 e 23!")

