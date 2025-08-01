# Controle de Estoque em Python

Esse sistema de controle de estoque foi feito em Pyhton com os sequintes requisitos:

* Cadastrar produtos
* Listar produtos em estoque
* Atualizar quantidades
* Aplicar descontos nos produtos
* verificar o valor total em estoque
* 
---

### 🛠 Sistema:

<img width="432" height="215" alt="image" src="https://github.com/user-attachments/assets/49e7f69a-cb59-4698-83df-102564739098" />

---

### Código

produtos: Dicionário que armazena os produtos, onde a chave é o ID e o valor é um dicionário com nome, quantidade e preço.
função | ação
-------|------
menuProd() | <font size="2"> menu de opções</font>
addProduto() | <font size="2"> inclui novo produto, preço e qualtidade </font>
buscarProduto(nProduto) | <font size="2"> busca um produto pelo seu nome </font>
atualizarQtd() | <font size="2"> atualiza a quantidade em estoque </font>
aplicarDesconto() | <font size="2"> aplica desconto optado pelo usuário </font>
repetirAcao(acao) | <font size="2"> repete a ação atual até que o usuário não queira mais realizá-la</font>
exibirTotal() | <font size="2"> exite o total em estoque </font>
listarProdutos() | <font size="2"> retorna uma lista de nomes de produtos, quantidades e preço </font>

