while True:
    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro número: ")
    operador = input("Digite um operador (+-/*): ")

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print("Um ou mais números não são válidos.")    
        continue

    operadores_permitidos = '+-/*'
       
    if len(operador) > 1:
        print("Digite apenas um operador.")
        continue
    
    if operador not in operadores_permitidos:
        print("O operador não é permitido.")
        continue

    print("Realizando sua conta, confira o resultado abaixo:")

    if operador == '+':
        print(f'{num_1_float}+{num_2_float} =', num_1_float + num_2_float)
    if operador == '-':
        print(f'{num_1_float}-{num_2_float}=', num_1_float - num_2_float)
    if operador == '*':
        print(f'{num_1_float}*{num_2_float}=', num_1_float * num_2_float)
    if operador == '/':
        print(f'{num_1_float}/{num_2_float}=', num_1_float / num_2_float)

    sair = input("Você quer sair? [s]im: ").lower().startswith("s")

    if sair is True:
        print("Obrigado por participar!")
        break

    else:
        continue