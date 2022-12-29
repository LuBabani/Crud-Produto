from inclusao import incluir
from alteracao import alterar
from exclusao import excluir
from listagem import listar

banco = {} #criando dicionario publico

#definição da função
def menu():
    while True: 
        print ('*' * 35)
        print ('1 - Inclusão de produtos')
        print ('2 - Alteração de dados do produto')
        print ('3 - Exclusão de produto')
        print ('4 - Listagem de produto')
        print ('*' * 35)
        print ('S - Sair')

        escolha = input('')

        global banco
        if escolha == '1':
            banco = incluir(banco)
        elif escolha == '2':
            pass
            alterar()
        elif escolha == '3':
            pass
            excluir()
        elif escolha == '4':
            pass
            listar(banco)
        elif escolha.upper() == 'S':
            break
            
        else:
            print ('Opção Inválida!')
    #End while
#end menu
