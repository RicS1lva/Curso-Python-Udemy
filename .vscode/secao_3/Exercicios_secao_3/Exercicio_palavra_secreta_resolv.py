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

saudacao = input("Gostaria de jogar 'Jogo da forca'? [s]im [n]ão: ").lower().startswith('s')

palavra_secreta = "formidavel"
letras_acertadas = ''

tentativas = 0
limite_tentativas = 15

if saudacao:
    
    print("Vamos lá, você tem 15 tentativas.")
    while saudacao:
        
        letra_digitada = input("Digite uma letra: ")
        letra_invalida = letra_digitada.isnumeric()
        tentativas += 1
        tentativas_restantes = int(limite_tentativas) - int(tentativas)
        
        if tentativas > 15:
            print("Você esgotou as tentativas")
            print(f'A palavra secreta era {palavra_secreta}')
        
            break

        if letra_invalida:
            print("Digite apenas letras.")

        if len(letra_digitada) > 1:
            print("Digite apenas uma letra")
        
        if letra_digitada in palavra_secreta:
            letras_acertadas += letra_digitada
        
        palavra_formada = ''

        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '*'
        print('')
        print(palavra_formada)
        print(f'Você tem mais {tentativas_restantes} tentativas.')

        if palavra_formada == palavra_secreta:
            print("PARABÉNS, VOCÊ GANHOU!")
            print(f'A palavra secreta era "{palavra_secreta}"')
            print(f'Você concluiu o jogo em {tentativas} tentativas.')
            break

else:
    print("Tudo bem.")
    print("Até a proxima!")


















