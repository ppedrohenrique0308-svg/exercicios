def validar_senha(senha): 
    if len(senha) < 8:
        senha = False
        return False
    tem_numero = False
    tem_maiuscula = False
    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.isdigit():
            tem_numero = True
    return tem_maiuscula and tem_numero

while True:
    senha_digitada = input('digite uma senha: ')
    if validar_senha(senha_digitada):
        print('senha valida')
        break
    else:
        print("errado")
print('terminou')