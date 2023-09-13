"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é (nome)
        Seu nome invertido é (nome invertido)
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    Exiba "Desculpe, você deixou campos vazios"
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
espaco = " "
quantidade_letras = len(nome)
penultima_letra = int(quantidade_letras) - 1

if nome != ("") and idade != (""):
    print('oi')
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é:{nome[quantidade_letras: :-1]}')
    if espaco in nome:
        print(f'Seu nome contém espaços')
    if espaco not in nome:
        print(f'Seu nome não contém espaços')
    print(f'Seu nome contém', quantidade_letras, 'letras')
    print(f'A primeira letra do seu nome é:', nome[0:1])
    print(f'A última letra do seu nome é:', nome[penultima_letra:quantidade_letras])
        

else:
    print('Você deixou campos vazios')



