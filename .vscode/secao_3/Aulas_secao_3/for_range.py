"""
Iterável -> str, range, etc (___iter___)
Iterador -> quem sabe entregar um valor por vez
next-> me entregue o proximo valor
iter -> me entregue seu iterador
"""

texto = 'Luiz'

for letra in texto:
    print(letra)

#O dois códigos fazem a mesma coisa.
#O For executa exatamente esta função de iteração abaixo:

texto = 'Luiz'
iterador = iter(texto)

while True:

    try:
        letra = next(iterador)
        print(letra)
        
    except StopIteration:
        break
