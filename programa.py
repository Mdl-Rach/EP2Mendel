import funcoes
cartela = {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}
lista_categorias = ['1','2','3','4','5','6','sem_combinacao','quadra','full_house','sequencia_baixa','sequencia_alta','cinco_iguais']
rodada = 1
lista_dados = [0, 0, 0, 0, 0]
lista_n_2 = ['1', '2', '3', '4', '5', '6']
lista_n = [1, 2, 3, 4, 5, 6]
lista_x = ['sem_combinacao','quadra','full_house','sequencia_baixa','sequencia_alta','cinco_iguais']
guardados = []
while rodada <= 12:
    rodou = 1
    w = 0
    for a_s, dicio in cartela.items():
        for categoria, valor in dicio.items():
            if valor == -1:
                w = 1
                break
    if w == 0:
        break
    lista_dados = funcoes.rolar_dados(len(lista_dados))
    print (f'dados rolados {lista_dados}')
    print (f'dados guardados {guardados}')
    print ("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    option = input('> ')
    while option != '0':
        if option == '1':
            print ("Digite o índice do dado a ser guardado (0 a 4):")
            n_dado = int(input('> '))
            dados_rodada = funcoes.guardar_dado (lista_dados, guardados, n_dado)
            lista_dados = dados_rodada [0]
            guardados = dados_rodada [1]
            print (f'dados rolados {lista_dados}')
            print (f'dados guardados {guardados}')
            print ("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            option = input('> ')
        elif option == '2':
            print ("Digite o índice do dado a ser guardado (0 a 4):")
            n_dado = int(input('> '))
            dados_rodada = funcoes.remover_dado (lista_dados, guardados, n_dado)
            lista_dados = dados_rodada [0]
            guardados = dados_rodada [1]
            print (f'dados rolados {lista_dados}')
            print (f'dados guardados {guardados}')
            print ("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            option = input('> ')
        elif option == '3':
            rodou += 1
            if rodou > 3:
                print ("Você já usou todas as rerrolagens.")
                print (f'dados rolados {lista_dados}')
                print (f'dados guardados {guardados}')
                print ("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
                option = input('> ')
            else:
                lista_dados = funcoes.rolar_dados(len(lista_dados))
                print (f'dados rolados {lista_dados}')
                print (f'dados guardados {guardados}')
                print ("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
                option = input('> ')
        elif option == '4':
            funcoes.imprime_cartela(cartela)
            print (f'dados rolados {lista_dados}')
            print (f'dados guardados {guardados}')
            print ("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            option = input('> ')
        else:
            print ( "Opção inválida. Tente novamente.")
            option = input('> ')


    if option == '0':
        lista_dados += guardados
        print ("Digite a combinação desejada:")
        checa_categoria = -1
        #laço
        while checa_categoria == -1:
            categoria = input("> ")
            while categoria not in lista_categorias:
                print ("Combinação inválida. Tente novamente.")
                categoria = input("> ")
            if categoria in lista_n_2:
                for i in range (7):
                    if categoria == f'{i}':
                        categoria = i
            # laço para ver se categoria está ocupada
            for regra, dicio in cartela.items():
                for categorias, valor in dicio.items():
                    if categoria in lista_n:
                        if categoria == categorias:
                            if valor != -1:
                                print ("Essa combinação já foi utilizada.")
                                checa_categoria = -1
                                break
                            else:
                                funcoes.faz_jogada(lista_dados, categoria, cartela)
                                lista_dados = [0, 0, 0, 0, 0]
                                guardados = []
                                checa_categoria = 0
                                break
                    if categoria in lista_x:
                        if categoria == categorias:
                            if valor != -1:
                                print ("Essa combinação já foi utilizada.")
                                checa_categoria = -1
                                break
                            else:
                                funcoes.faz_jogada(lista_dados, categoria, cartela)
                                lista_dados = [0, 0, 0, 0, 0]
                                guardados = []
                                checa_categoria = 0
                                break
    rodada += 1
pontuação = 0
for regras, dicio in cartela.items():
    for categoria, valor in dicio.items():
        pontuação += valor

pontuação_simples = 0
for regras, dicio in cartela.items():
    if regras == 'regra_simples':
        for categoria, valor in dicio.items():
                pontuação_simples += valor

if pontuação_simples >= 63:
    pontuação += 35

funcoes.imprime_cartela(cartela)
print (f"Pontuação total: {pontuação}")