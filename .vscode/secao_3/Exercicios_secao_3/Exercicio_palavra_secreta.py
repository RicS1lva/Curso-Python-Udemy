"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer
 e vai dar a possibilidade para o usuário digitar apenas
 uma letra.
 - Quando o usuário digitar uma letra, você vai conferir
 se a letra digitada está na palavra secreta.
 - Se a letra digitada estiver na palavra secreta;
 exiba a letra;
 - Se a letra digitada não estiver na palavra secreta; exiba*
 Faça a contagem de tentativas do usuário.
 """

apresentacao = input("Gostaria de iniciar o jogo? [s}im [n]ão: ").lower().startswith('s')

if apresentacao:
    print("Bem-vindo ao jogo da forca! Basta digitar uma letra por vez, até adivinhar qual a palavra secreta.")
    print("Vamos começar!")
    contador = 0
    letra_digitada = input("Digite uma letra: ").lower()
    letra_is_str = letra_digitada.isnumeric()
    palavra_secreta = "piracicaba"
    
    while True:

        if letra_is_str is True:
            print("Digite apenas letras!")
            continue

        if len(letra_digitada) > 1:
            print("Digite apenas uma letra!")

        if letra_digitada in palavra_secreta:
            print(palavra_codigo)
            contador += 1

        if letra_digitada not in palavra_secreta:
            ...
            contador += 1
            


















else:
    print("Tudo bem, até a próxima!")