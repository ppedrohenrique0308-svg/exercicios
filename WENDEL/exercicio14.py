ni = float(input('escreva seu salario: R$'))
if ni <= 1500 or 3000 :
    salario = ni * (15/100+1)
    if ni > 3000:
        salario = ni * (5/100+1)
print(f'seu novo salario vai ser de {salario:.2f}')