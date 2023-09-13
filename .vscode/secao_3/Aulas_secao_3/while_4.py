"""
Repetições
While (enquanto)
Executa uma ação  enquanto uma condição for verdadeira
Loop infinito -> quando o código não tem fim

continue = ele para a função e volta ao while
"""

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    
    while coluna <= qtd_colunas:
        print(linha, coluna)
        coluna += 1

    linha += 1

print("Acabou")
