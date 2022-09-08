# Identificador se encontra no início da Main
lista_pecas = []


# --------Começo da função cadastrarPeca---------
def cadastrarPeca(codigo):
    print('Você selecionou a opção de Cadastrar Peça')
    print('Código da Peça {}'.format(codigo))
    # início da entrada dos dados
    nome = input('Por favor entre com o NOME da peça: ')
    fabricante = input('Por favor entre com o FABRICANTE da peça: ')
    valor = float(input('Por favor entre com o VALOR(R$) da peça: '))
    # fim da entrada dos dados
    dicionariocodigo = {'codigo': codigo,  # dicionário
                        'nome': nome,
                        'fabricante': fabricante,
                        'valor': valor}
    lista_pecas.append(dicionariocodigo.copy())


# ---------Final da função cadastrarPeca--------

# --------Começo da função consultarPeca--------
def consultarPeca():
    print('Você selecionou a opção de Consultar Peça')
    while True:
        try:
            opcaoConsultar = int(input(
                'Escolha a opção desejada:\n1-Consultar Todas as Peças\n2-Consultar Peças por Código\n3-Consultar Peças por Fabricante\n4-Retornar\n>>'))
            if opcaoConsultar == 1:
                print('-' * 41)
                for codigo in lista_pecas:  # selecionar cada dicionário da minha lista (cada peça da lista de peças)
                    for key, value in codigo.items():  # selecionar cada conjunto chave : valor do dicionário
                        print('{} : {}'.format(key, value))  # print chave, valor
                    print('-' * 41)
            elif opcaoConsultar == 2:
                entrada = int(input('Digite o CÓDIGO da Peça: '))  # entrada para consultar peça por código
                print('-' * 41)
                for codigo in lista_pecas:
                    if (codigo['codigo'] == entrada):
                        for key, value in codigo.items():
                            print('{} : {}'.format(key, value))  # print chave, valor
                        print('-' * 41)
            elif opcaoConsultar == 3:
                entrada = input('Digite o FABRICANTE da Peça: ')  # entrada para consultar peça por fabricante
                print('-' * 41)
                for codigo in lista_pecas:
                    if (codigo['fabricante'] == entrada):
                        for key, value in codigo.items():
                            print('{} : {}'.format(key, value))  # print chave, valor
                        print('-' * 41)
            elif opcaoConsultar == 4:  # retornar ao menu anterior
                print('-' * 41)
                print('Você optou por retornar. Retornando...')
                return
            else:
                print('Pare de digitar números que não existem no menu')
                continue
        except ValueError:
            print('Pare de digitar valores não inteiros')
            break


# --------Final da função consultarPeca--------

# --------Começo da função removerPeca--------
def removerPeca():
    print('Você selecionou a opção de Remover Peça')
    entrada = int(input('Digite o CÓDIGO da peça a ser removida: '))  # remover peça através do código
    for codigo in lista_pecas:
        if (codigo['codigo'] == entrada):
            lista_pecas.remove(codigo)


# --------Final da função removerPeca--------

# --------Começo da Main--------
print('Bem Vindo ao Controle de Estoques da Bicicletaria do Paulo Vinicius Sales Moura')
codigo_peca = 0
while True:
    try:
        opcao = int(
            input('Escolha a opção desejada:\n1-Cadastrar Peças\n2-Consultar Peças\n3-Remover Peças\n4-Sair\n>>'))
        if opcao == 1:
            codigo_peca = codigo_peca + 1
            cadastrarPeca(codigo_peca)
        elif opcao == 2:
            consultarPeca()
        elif opcao == 3:
            removerPeca()
        elif opcao == 4:
            print('Você optou por sair do programa. Programa finalizado...')
            break
        else:
            print('Pare de digitar números que não existem no menu')
            continue
    except:
        print('Pare de digitar valores não inteiros')
        break
    # --------Fim da Main-------------
