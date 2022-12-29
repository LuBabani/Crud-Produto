def incluir(bancoDados):
    print('***Inclusão de Produto***\n')

    codigo = int(input('Digite o codigo do produto: '))

    nome = input('Nome do produto: ')
    preco = float(input('Valor: '))
    qt = float(input('Quantidade: '))
    qtMin = float(input('Quantidade mínima: '))
    
    listaproduto = [nome, preco, qt, qtMin]
    bancoDados [codigo] = listaproduto

   
    return bancoDados


 #como criar lista: nomeDaLista = []  
 #como criar lista2: nomeDaLista = list()
 #como criar lista3: nomeDaLista = [1, 2, 3, 'Porca', False, 3.14]

#como criar Dicionario: bancoDados = {}
#como criar dicionario2 bancoDados = dict()
