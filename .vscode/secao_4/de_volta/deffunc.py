'''
Introdução às funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores parâmetros (argumentos)
e retornat um valor específico.
Por padrão, funções Python retornam None (nada)
'''
numero1 = input('Olá, diga um número inteiro')
numero2 = input('Agora diga outro número inteiro')



def imprimir(a, b):
    print(f'A soma dos dois números é {a + b}')
    

    
imprimir(int(numero1), int(numero2))


