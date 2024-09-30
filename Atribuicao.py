repeat = True

def calcular_boleto():
    repeat = True  # Definindo o repeat para garantir pq sim né
    while repeat:
        saldo = float(input("Seu saldo? "))
        boleto = float(input("Seu boleto? "))
        operacao = input("Escolha se é Multiplicação, Divisão, Subtração ou Adição ").lower()

        if operacao == "adicao":
            print(f"Seu saldo era de {saldo} e seu boleto a pagar é de {boleto}. Seu saldo agora é de {saldo + boleto}")
            repeat = False
        elif operacao == "subtracao":
            print(f"Seu saldo era de {saldo} e seu boleto a pagar é de {boleto}. Seu saldo agora é de {saldo - boleto}")
            repeat = False
        elif operacao == "divisao":
            if boleto != 0:
                print(f"Seu saldo era de {saldo} e seu boleto a pagar é de {boleto}. Seu saldo agora é de {saldo / boleto}")
            else:
                print("Não é possível dividir por zero!")
            repeat = False
        elif operacao == "multiplicacao":
            print(f"Seu saldo era de {saldo} e seu boleto a pagar é de {boleto}. Seu saldo agora é de {saldo * boleto}")
            repeat = False
        else:
            print("Operação inválida, tente novamente.")

def calcular_valores():
    repeat = True  # Variável para continuar o loop
    while repeat:
        x = float(input("Primeiro valor? "))
        pergunta1 = input("Qual operação do primeiro valor com o do segundo? X, +, -? ").lower()
        
        y = float(input("Segundo valor? "))
        pergunta2 = input("Qual a operação do segundo valor com o do terceiro? X, +, -? ").lower()
        
        z = float(input("Terceiro valor? "))  # Sempre pedir o terceiro valor

        # Operações resumidas
        if pergunta1 == "x" or pergunta1 == "multiplicacao":
            resultado1 = x * y
        elif pergunta1 == "+" or pergunta1 == "adicao":
            resultado1 = x + y
        elif pergunta1 == "-" or pergunta1 == "subtracao":
            resultado1 = x - y
        else:
            print("Operação inválida!")
            continue

        # Segunda operação entre resultado1 e z
        if pergunta2 == "x" or pergunta2 == "multiplicacao":
            resultado_final = resultado1 * z
        elif pergunta2 == "+" or pergunta2 == "adicao":
            resultado_final = resultado1 + z
        elif pergunta2 == "-" or pergunta2 == "subtracao":
            resultado_final = resultado1 - z
        else:
            print("Operação inválida!")
            continue

        print(f"O resultado final é {resultado_final}")
        
        repeat = input("Deseja repetir? (s/n): ").lower() == 's'

def opcoes():
    repeat = True
    while repeat:
        print("Você pode escolher:")
