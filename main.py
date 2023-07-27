def soma(valor1, valor2):
    return valor1+valor2

def subtrai(valor1,valor2):
    return valor1-valor2

def multiplica(valor1,valor2):
    return valor1*valor2

def divide(valor1,valor2):
    if valor2==0: 
        print('Não pode dividir!')
    return valor1/valor2

def menu():
    print("1. Soma")
    print("2. Subtrai")
    print("3. Multiplica")
    print("4. Divide")
    print("5. SAIR")

while True:
    menu()
    print("Digite os valores: ")
    valor1 = input("Qual o valor1? ")
    valor2 = input("Qual o valor2? ")
    opcao = input("Qual a opção de operação? ")
    if opcao=='1':
        resultado = soma(valor1, valor2)
        print(f'Resultado da soma: {resultado}')
    elif opcao=='2':
        resultado = subtrai(valor1, valor2)
        print(f'Resultado da subtração: {resultado}')
    elif opcao=='3':
        resultado = multiplica(valor1, valor2)
        print(f'Resultado da multiplicação: {resultado}')
    elif opcao=='4':
        resultado = divide(valor1, valor2)
        print(f'Resultado da divisão: {resultado}')
    elif opcao=='5':
        break
    else:
        print('Oção inválida')