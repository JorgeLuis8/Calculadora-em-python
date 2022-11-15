while True:
    print("-----------------CALCULADORA-----------------")
    print("INFORME OS VALORES A SEGUIR: ")

    num_1=input('Digite o numero')
    num_2=input('Digite outro numero')
    print("ADIÇÂO(+)")
    print("SUBTRAÇÃO(-)")
    print("MULTIPLICAÇÃO(*)")
    print("DIVISÃO(/)")
    sinal=input('Informe o operacao')
    num_1=float(num_1)
    num_2=float(num_2)
    
    if sinal == '+':
        print(num_1+num_2)
    elif sinal == '-':
        print(num_1-num_2)
    elif sinal == '*':
        print(num_1*num_2)    
    elif sinal =='/':
        print(num_1/num_2)
    elif sinal =='S':
        break
    else:
        print("Operador invalido")

print('Calculadora Finalizada')