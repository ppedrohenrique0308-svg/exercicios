def calculadora():
    ni = int(input('digite: '))
    n1 = int(input('digite: '))
    n2 = str(input('qual calculo: '))
    if n2 == "+":
        print(ni+n1)
    elif n2 == "-":
        print(ni-n1)
    elif n2 == "*":
        print(ni*n1)
    elif n2 == "/":
        print(ni/n1)
calculadora()