# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
#São considerados falsy (que vc ja viu)
# 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor
# or - Qualquer avaliação verdadeira avalia
#toda a expressão como verdadeira.
 
'''
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
'''

#Avaliação de curto circuito

Senha = input('Insinra sua senha: ') or 'Sem senha'
print(Senha)

#print(True and 0 and True)
#print(True or False)
#
#print(0 or False or 0 or 'abc' or True)
