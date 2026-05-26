peso = int(input('peso: '))
altura = float(input('altura: '))
imc = peso / altura**2
print(f'o seu imc é {imc:.2f}')
if imc <= 18.5 :
    print('abaixo do peso')
elif imc > 18.5 < 24.9:
    print('peso normal')
elif 25 < imc < 29.9:
    print('sobre peso')
else:
    print('obesidade')