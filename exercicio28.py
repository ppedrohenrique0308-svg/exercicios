def menu():
    print('--'*15)
    print('1 - Adicionar contado')
    print('2 - Remover contato')
    print('3 - buscar telefone pelo nome')
    print('4 - listar todos')
    print('0 - sair')
    opcao = int(input('escolha uma das opçao: '))
    print('--'*15)
    if opcao >= 0 and opcao <= 4:
       return opcao
    else :
        print('opçao nao encontrada')

def adicionar_c(agenda):
    nome = input('digite o nome: ')
    telefone = input('digite o numero: ')
    agenda[nome] = telefone
    print('adicionado contato')
    return agenda

if __name__ == "__main__": 
    agenda = {}
    opcao = menu()

    while opcao != 0 :
        if opcao == 1:
            agenda = adicionar_c(agenda)
        elif opcao == 2:
            nome = input('digite o nome para remover: ')
            if nome in agenda:
                del agenda[nome]
                print('contato removido')
            else:
                print('contato nao encontrado')
        elif opcao == 3:
            nome = input('buscar o telefone pelo nome: ')
            if nome in agenda:
                print(f'telefone: {agenda[nome]}')
            else:
                print('contato nao encontrado')
        elif opcao == 4:
            if not agenda:
                print('a agenda esta vazia')
            else:
                for nome, telefone in agenda.items():
                    print(f"{nome}: {telefone}")
        opcao = menu()

        