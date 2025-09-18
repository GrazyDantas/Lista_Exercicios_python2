#implemente um conversor de bases numéricas (decimal, binário, octal, hexadecimal) com validação.

try:
    num = int(input("Digite o número que deseja converter: "))
    if (num > 0):
        num = str(num)
        decimal = "{0},{1}{1}".format(num, 0)
        print("Decimal:",decimal)
        num = int(num)
        binario = num % 2
        print("Binário:",binario)
        octal = num / 8
        print("Octal:",octal)
        hexadecimal = num / 16
        print("Hexadecimal:",hexadecimal)
    else:
        print("Digite números maiores que zero")
except:
    print("Digite apenas números")
