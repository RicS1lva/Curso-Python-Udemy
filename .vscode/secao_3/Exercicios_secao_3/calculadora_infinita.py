while True:
    saudacao = input("Gostaria de usar nossa calculadora? [s]im - [n]ão: ").lower().startswith('s')
    numeros_validos = None
    numero_um = 0
    numero_dois = 0
    operadores_validos = '+-*/' 


    if saudacao:
        
        print("Bem vindo!")
        print("Vamos começar!")

        while True: 
        
            numero_um = input("Digite um número: ")
            numero_dois = input("Digite outro número: ")
            operador = input("Escolha um operador entre +(Adição), -(Subtração, *(Multiplicação) e /(Divisão): ")

            try:
                numero_um_float = float(numero_um)
                numero_dois_float = float(numero_dois)
                numeros_validos = True
            
            except:
                numeros_validos = None

            if numeros_validos is None:
                print("Um ou ambos os números são inválidos!")
                continuar = input("Vamos tentar denovo? [s]im - [n]ão: ").lower().startswith("s")
                if continuar:
                    continue
                else:
                    break

            if len(operador) > 1:
                print("Digite apenas um operador!")
                continuar = input("Vamos tentar denovo? [s]im - [n]ão: ").lower().startswith("s")
                if continuar:
                    continue
                else:
                    break
                continue
            if operador not in operadores_validos:
                print("Operador inválido!")
                continuar = input("Vamos tentar denovo? [s]im - [n]ão: ").lower().startswith("s")
                if continuar:
                    continue
                else:
                    break
                
            

            print("Realizamos sua conta!")
            print("Confira o resultado abaixo")

            if operador == "+":
                print(f'{numero_um_float} + {numero_dois_float} = ', numero_um_float + numero_dois_float)
            if operador == "-":
                print(f'{numero_um_float} - {numero_dois_float} = ', numero_um_float - numero_dois_float)
            if operador == "*":
                print(f'{numero_um_float} * {numero_dois_float} = ', numero_um_float * numero_dois_float)
            if operador == "/":
                print(f'{numero_um_float} / {numero_dois_float} = ', numero_um_float / numero_dois_float)
            
            sair = input("Gostaria de sair da calculadora? [s]im - [n]ão: ").lower().startswith('s')

             



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    else:
        print("Sem problemas, até logo!")
        break