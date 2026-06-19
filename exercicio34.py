def calcular_imc(peso, altura):
    result = peso / (altura*2)
    return result

def classificar_imc(imc):
    if imc < 18.5 :
            print('baixo do peso')
    elif imc >= 18.5 and imc < 25 :
            print('peso normal')
    elif imc >= 25 and imc < 30 :
            print('excesso de peso')
    elif imc >= 30 and imc < 35:
        print('obesidade')
    else:
            print('obesidade extrema')

peso = float(input('me fale seu peso: '))
altura = float(input('me informe sua altura: '))
imc = calcular_imc(peso, altura)
classificar_imc(imc)
