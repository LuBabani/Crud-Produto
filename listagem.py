def listar(bd):
    print ('***Lista de produtos***')
    for chave in bd:
            print(f'{chave} - {bd[chave][0]} - {bd[chave][1]} - {bd[chave][2]} - {bd[chave][3]} ')
