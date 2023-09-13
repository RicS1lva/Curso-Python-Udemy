nome = input("Qual seu nome?: ")
altura = input("Qual a sua altura? (em metros): ")
peso = input("Qual o seu peso? (em quilos): ")
imc = float(peso) / (float(altura) ** 2)

print(nome, 'tem', (str(altura) + 'm'), "de altura")
print('pesa', (str(peso) + 'kg'), 'e seu IMC é')
print(f'{imc:.2f}')

