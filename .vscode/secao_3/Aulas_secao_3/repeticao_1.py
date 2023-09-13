"""
Repetições
While (enquanto)
Executa uma ação  enquanto uma condição for verdadeira
"""

condicao = True

while condicao:
    nome = input("Qual o seu nome? ")
    if nome == "sair": 
        break
    print(f'Seu nome é {nome}')

    
print("Saiu.")