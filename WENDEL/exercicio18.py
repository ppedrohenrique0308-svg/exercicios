import random
escolhido = random.randint(1,10)
for c in range(1,3+1):
    ni = int(input('escreva: '))
if ni == escolhido :
        print(f'acertou {escolhido}')
else:
        print(f'errou {escolhido}')
