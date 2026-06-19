ni = 0
while True:
    try:
        ni = int(input('digite sua idade: '))
        break
    except:
        print('idade incorreta')
print('terminou')