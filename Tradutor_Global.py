 
#input do usuario
Decisao_1 = int(input('Digite o que quer, Decifrar(1) ou criptografar(2): '))
Decisao_2 = int(input('Digite o que quer, Binario (2), Octal (8) ou Hexadecimal (16): '))
Num = input('Digite o Numero: ')

def Calcular_Binario (num, Decisao_1):
    if Decisao_1 == 2:
        num = int(num)
        binario = bin(num)
        binario_sem = binario[2:]
        return binario_sem
    else: 
        Normal = int(num, 2)
        return str(Normal)

def Calcular_Octal (num, Decisao_1): 
    if Decisao_1 == 2:
        num = int(num)
        Octal = oct(num)
        Octal_sem = Octal[2:]
        return Octal_sem 
    else:
        Normal = int(num, 8)
        return str(Normal)

def Calcular_Hexadecimal (num, Decisao_1):
    if Decisao_1 == 2:
        num = int(num)
        Hexadecimal = hex(num)
        Hexadecimal_sem = Hexadecimal[2:]
        return Hexadecimal_sem
    else:
        Normal = int(num, 16)
        return str(Normal)

if Decisao_2 == 2:
    #sai o numero inteiro traduzido do binario
    Resultado = Calcular_Binario(Num, Decisao_1)
elif Decisao_2 == 8:
    #sai o numero inteiro traduzido do octal
    Resultado = Calcular_Octal(Num, Decisao_1)
elif Decisao_2 == 16:
    #sai o numero inteiro traduzid do hexadecimal
    Resultado = Calcular_Hexadecimal(Num, Decisao_1)
else:
    print('Pedido invalido')

print('seu numero é :', Resultado)
