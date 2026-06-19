try:
    ni = int(input("ditite um numero: "))
    n1 = int(input("digite outro numero: "))
    s = ni / n1
    print(f'a divisao entre {ni} e {n1} é {s}')
except ZeroDivisionError:
    print('voce tentou dividir zero')