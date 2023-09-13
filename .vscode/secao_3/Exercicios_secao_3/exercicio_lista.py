
import os 
menu_resposta = True
lista_compras = [] 


while menu_resposta:
    menu_resposta = input("Selecione uma opção:\
    [i]nserir [a]pagar [l]istar: ").lower()
    respostas_validas = ["i", "a", "l"]
    indices = range(len(lista_compras))

    if menu_resposta == "i":
        item_add = input("Qual item deseja incluir?: ")
        
        if item_add in lista_compras:
            print("Este item ja foi adicionado")
            continue
        else:
            lista_compras.append(item_add)
            print(f'{item_add} foi incluído na lista de compras.')
    
    if menu_resposta == "a":
        apagar_indice = input("Qual índice deseja apagar?: ").isnumeric()
        
        if apagar_indice:
            int(apagar_indice)
            if apagar_indice in indices:
                del lista_compras[apagar_indice]
                print(f'O item "{lista_compras[apagar_indice]}" foi apagado da lista')

            else:
                print("Por favor insira um índice existente.")
                continue
            

        else:
            print("índice inexistente")
        
    if menu_resposta == "l":
        for indice, nome in enumerate(lista_compras):
            print(indice, nome)
            continue


    if menu_resposta not in respostas_validas:
        print("opção inválida")
        
    