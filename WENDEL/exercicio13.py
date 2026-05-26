ni = int(input('escreva: '))
n2 = int(input('escreva: '))
n3 = int(input('escreva: '))
if ni == n2 == n3:
    print('equilatero')
elif ni == n2 or ni == n3 or n2 == n3 :
            print('isoceles')
else:
      print('escaleno')