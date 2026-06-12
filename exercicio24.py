# exercicio extra
lista = []
ni = int(input('digite: '))
lista.append(ni)
continuar = str(input('escreva:'))
if continuar == 's':
        while continuar == 's':
            n1 = int(input('digite: '))
            lista.append(n1)
            continuar = str(input('escreva: '))
elif continuar == 'n': 
      print(f'voce escolheu um numero na lista e foi o {lista}')
print(f'voce escolheu os seguintes numeros: {lista}')