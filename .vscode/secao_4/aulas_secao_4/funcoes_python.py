"""
Introdução as funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetro (argumentos)
e retornar um valor específico.
Por padrão, funções python retornam None (nada).
"""

"""
Parâmetro = variáveis definidas dentro da função
Argumento = valores passador no chamado da função
"""
# def imprimir(a, b, c):
#     print(a, b, c)

# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao(nome= "Sem nome"):
    print(f'Olá, {nome}')

saudacao("Ricardo")
saudacao("Fernanda")
saudacao("Miryan")
saudacao()


