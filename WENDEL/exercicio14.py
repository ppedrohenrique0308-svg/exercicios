ni = float(input('escreva seu salario: R$'))
if ni < 1500 :
    salario = ni * (15/100+1)
elif 1500 <= ni <= 3000 : 
    salario = ni * (10/100+1)
else:
    salario = ni * (5/100+1)
print(f'seu novo salario vai ser de {salario:.2f}')