"""
Repetições
While (enquanto)
Executa uma ação  enquanto uma condição for verdadeira
Loop infinito -> quando o código não tem fim

continue = ele para a função e volta ao while
"""

contador = 0

while contador < 100:
    contador = contador + 1
    

    if contador == 6:
        print("Não vou mostrar o 6.")
        continue

    if contador >= 10 and contador <=20:
        print("Não vou mostrar o", contador)
        continue

    print(contador)

    if contador == 40:
        break

print("acabou")