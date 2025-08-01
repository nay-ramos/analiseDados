'''A RetailCo contratou um Desenvolvedor Python para criar um sistema de gerenciamento
 de estoque. O objetivo é controlar produtos, suas quantidades e preços, e permitir a
  aplicação de descontos. O sistema deve incluir funcionalidades como a atualização de
   estoque, exibição em tempo real dos itens disponíveis e cálculo do valor total. O
    desafio é implementar um menu interativo para otimizar a gestão, com opções de
    1 - adicionar produtos
    2 - atualizar quantidades
    3 - aplicar descontos
    4 - exibir o total do estoque.\n\n
    5 - Sair do menu'''
import time

prodList = {}
id_produto = 1

#Funções

# add produto produto à base de dados
def addProduto():
    global id_produto

    nome = input('Digite o nome do produto: ').strip().capitalize()
    preco = float(input('Digite o preço do produto: '))
    quantidade = int(input('Digite o quantidade do produto: '))

    prodList[id_produto] = {"nome": nome, "preco": preco, "quantidade": quantidade}

    print(prodList[id_produto].get("nome"), 'Foi cadastrado com sucesso!')
    id_produto += 1



# Buscar Produto por nome e retorna um id
def buscarProduto(nProduto):
    idProd = 0
    
    for id, dadosProd in prodList.items():
        if dadosProd["nome"] == nProduto:
            idProd = id
    
    return idProd



#atualizar qtd
def atualizarQtd():
    nProduto = input('Qual produto deseja alterar a quantidade: ').strip().capitalize()
    qtd = int(input('Qual a nova quantidade: '))

    if not prodList:
        print('\nSem produtos cadastrados!')

    else:
        idProd = buscarProduto(nProduto)

        if idProd == 0:
            print(f'\nProduto {nProduto} não encontrado!')
        else:
            for id, dadosProd in prodList.items():
                if id == idProd:
                    dadosProd["quantidade"] = qtd
                    print(f'\nO produto {nProduto} agora tem {dadosProd["quantidade"]} unidades registradas!\n')




#Substitui o preço pelo valor com desconto escolhido pelo usuario
def aplicarDesconto():
    nProduto = input('Qual produto deseja aplicar desconto? ').strip().capitalize()
    desconto = float(input('Qual o desconto (em %): '))

    #validação desconto
    while desconto not in range(1, 100):
        print(f'{desconto} não é um desconto válido, apenas aceitos descontos de 1% à 99%')
        desconto = float(input('Qual o desconto (em %): '))

    if not prodList:
        print('\nSem produtos cadastrados!')
    else:
        idProd = buscarProduto(nProduto)

        if idProd == 0:
            print(f'\nProduto {nProduto} não encontrado!')
        else:
            for id, dadosProd in prodList.items():
                if id == idProd:
                    dadosProd["preco"] *= (1-desconto/100)
                    print(f'\nO produto {nProduto} agora tem custa R${dadosProd["preco"]:.2f}!\n')



#repetir determinada ação antes de voltar pro menu até que o usuário não queira mais repetir
def repetirAcao(acao):
    denovo = 'S'

    while denovo[0] != 'N':
        print('\n' + '-' * 50)
        denovo = input(f'{acao} novamente [S/N]? ').strip().upper()
        print('-' * 50 + '\n')

        if denovo[0] == 'S':
            if acao == 'Cadastrar':
                addProduto()
            elif acao == 'Atualizar quantidade':
                atualizarQtd()
            elif acao =='Aplicar desconto':
                aplicarDesconto()

        elif denovo[0] == 'N':
            pass

        else:
            print("Opção inválida, voltando para Menu Inicial\n")
            time.sleep(1)
            denovo = 'N'
            pass

#exibir a soma de todos os produtos no estoque
def exibirTotal():
    totalEstoque = 0
    if not prodList:
        print('\nSem produtos cadastrados!')
    else:
        for id, dadosProd in prodList.items():
            totalEstoque += dadosProd["quantidade"]

        print(f'\n no momento existem {totalEstoque} produtos no estoque!\n')


# exibir a soma de todos os produtos no estoque
def listarProdutos():

    if not prodList:
        print('\nSem produtos cadastrados!')
    else:
        print(f'\n{"Lista de produtos cadastrados":*^50}')
        for id, dadosProd in prodList.items():
            print(f'''
                Id do produto: {id}
                Nome:{dadosProd["nome"]}
                Preço: {dadosProd["preco"]}
                Quantidade:{dadosProd["quantidade"]}
                
                {"":-<15}''')
            time.sleep(0.8)

#Menu
def menuProd():
    global prodList
    print(f'{"GERENCIAMENTO DE PRODUTOS":*^50}\n')
    print(f'*{"[1] Adicionar Produtos": ^50}*')
    print(f'*{"[2] Atualizar quantidade de produtos": ^50}*')
    print(f'*{"[3] Aplicar descontos": ^50}*')
    print(f'*{"[4] Exibir total estoque": ^50}*')
    print(f'*{"[5] Listar produtos": ^50}*')
    print(f'*{"[6] Sair do menu": ^50}*\n')
    print('*'*50)

    opcoes = input('O que deseja fazer? ')

    if opcoes == '1':
        acao = 'Cadastrar'
        addProduto()
        time.sleep(1)
        repetirAcao(acao)
        time.sleep(1)

    elif opcoes == '2':
        acao = 'Atualizar quantidade'
        atualizarQtd()
        time.sleep(1)
        repetirAcao(acao)
        time.sleep(1)

    elif opcoes == '3':
        acao = 'Aplicar desconto'
        aplicarDesconto()
        time.sleep(1)
        repetirAcao(acao)
        time.sleep(1)

    elif opcoes == '4':
        exibirTotal()
        time.sleep(4)

    elif opcoes == '5':
        listarProdutos()
        time.sleep(4)

    elif opcoes == '6':
        print('O sistema será encerrado, até a próxima!\n')
        time.sleep(1)
        breakpoint()
    else:
        print(f'a opção {opcoes} não é válida, voltando para Menu Inicial\n')
        time.sleep(2)

#Sistema
while True:
    menuProd()