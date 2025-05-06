import random
# Questão 1
def rolar_dados (n_dados):
    lista_dados = []
    for i in range (n_dados):
        lista_dados.append(random.randint(1,6))
    return lista_dados
# Questão 2
def guardar_dado (lista_mesa, lista_guardado, n_dado):
    lista_final = []
    lista_guardado.append(lista_mesa[n_dado])
    del lista_mesa [n_dado]
    lista_final.append(lista_mesa)
    lista_final.append(lista_guardado)
    return lista_final
# Questão 3
def remover_dado (lista_dados_rolados, lista_dados_guardados, n_dado):
    lista_final = []
    lista_dados_rolados.append(lista_dados_guardados[n_dado])
    del lista_dados_guardados[n_dado]
    lista_final.append(lista_dados_rolados)
    lista_final.append(lista_dados_guardados)
    return lista_final
# Questão 4
def calcula_pontos_regra_simples (lista_dados_rolados):
    dicionario = {}
    rascunho = [0]
    resultado = 0
    for i in range (len(lista_dados_rolados)):
        if lista_dados_rolados[i] == 1:
            rascunho.append(lista_dados_rolados[i])
    for a in range (len(rascunho)):
        resultado += rascunho[a]
        dicionario[1] = resultado
    rascunho = [0]
    resultado = 0
    for i in range (len(lista_dados_rolados)):
        if lista_dados_rolados[i] == 2:
            rascunho.append(lista_dados_rolados[i])
    for a in range (len(rascunho)):
        resultado += rascunho[a]
        dicionario[2] = resultado
    rascunho = [0]
    resultado = 0
    for i in range (len(lista_dados_rolados)):
        if lista_dados_rolados[i] == 3:
            rascunho.append(lista_dados_rolados[i])
    for a in range (len(rascunho)):
        resultado += rascunho[a]
        dicionario[3] = resultado
    rascunho = [0]
    resultado = 0
    for i in range (len(lista_dados_rolados)):
        if lista_dados_rolados[i] == 4:
            rascunho.append(lista_dados_rolados[i])
    for a in range (len(rascunho)):
        resultado += rascunho[a]
        dicionario[4] = resultado
    rascunho = [0]
    resultado = 0
    for i in range (len(lista_dados_rolados)):
        if lista_dados_rolados[i] == 5:
            rascunho.append(lista_dados_rolados[i])
    for a in range (len(rascunho)):
        resultado += rascunho[a]
        dicionario[5] = resultado
    rascunho = [0]
    resultado = 0
    for i in range (len(lista_dados_rolados)):
        if lista_dados_rolados[i] == 6:
            rascunho.append(lista_dados_rolados[i])
    for a in range (len(rascunho)):
        resultado += rascunho[a]
        dicionario[6] = resultado
    rascunho = [0]
    resultado = 0
    return dicionario
# Questão 5
def calcula_pontos_soma (lista_dados_rolados):
    resultado = 0
    for i in range (len(lista_dados_rolados)):
        resultado += lista_dados_rolados[i]
    return resultado
# Questão 6
def calcula_pontos_sequencia_baixa (lista_dados_rolados):
    comb_1 = [1, 2, 3, 4]
    comb_2 = [2, 3, 4, 5]
    comb_3 = [3, 4, 5, 6]
    for i in range (len(comb_1)):
        if comb_1[i] in lista_dados_rolados:
            x = 15
        else:
            x = 0
            break
    if x == 0:
        for i in range (len(comb_2)):
            if comb_2[i] in lista_dados_rolados:
                x = 15
            else:
                x = 0
                break
    if x == 0:
        for i in range (len(comb_3)):
            if comb_3[i] in lista_dados_rolados:
                x = 15
            else:
                x = 0
                break
    return x
# Questão 7
def calcula_pontos_sequencia_alta (lista_dados_rolados):
    comb_1 = [1, 2, 3, 4, 5]
    comb_2 = [2, 3, 4, 5, 6]
    for i in range (len(comb_1)):
        if comb_1[i] in lista_dados_rolados:
            x = 30
        else:
            x = 0
            break
    if x == 0:
        for i in range (len(comb_2)):
            if comb_2[i] in lista_dados_rolados:
                x = 30
            else:
                x = 0
                break
    return x
# Questão 8
def calcula_pontos_full_house (lista_dados_rolados):
    lista_a = [lista_dados_rolados[0]]
    lista_b = []
    resultado = 0
    i = 1
    while i < (len(lista_dados_rolados)):
        if lista_dados_rolados [i] == lista_a [0]:
            lista_a.append(lista_dados_rolados[i])
        elif lista_b == []:
            lista_b.append(lista_dados_rolados[i])
        elif lista_dados_rolados [i] == lista_b [0]:
            lista_b.append(lista_dados_rolados[i])
        else:
            x = 0
            break
        i += 1
    if len(lista_a) < 2 or len(lista_a) > 3:
        return 0
    if len(lista_b) < 2 or len(lista_b) > 3: 
        return 0
    if len(lista_a) == 2 and len(lista_b) == 3:
        for i in range (len(lista_dados_rolados)):
            resultado += lista_dados_rolados [i]
    if len(lista_b) == 2 and len(lista_a) == 3:
        for i in range (len(lista_dados_rolados)):
            resultado += lista_dados_rolados [i]
    return resultado
# Questão 9
def calcula_pontos_quadra (lista_dados_rolados):
    resultado = 0
    j = 0
    dicionario = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    for a in range (len(lista_dados_rolados)):
        for i in range (7):
            if  i == lista_dados_rolados[a]:
                for chave, lista in dicionario.items():
                    if chave == i:
                        lista.append(i)
    for chave, lista in dicionario.items():
        if len(lista) >= 4:
            j = 1
    if j == 1:
        for i in range (len(lista_dados_rolados)):
            resultado += lista_dados_rolados [i]
    return resultado
# Questão 10
def calcula_pontos_quina (lista_dados_rolados):
    resultado = 0
    j = 0
    dicionario = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    for a in range (len(lista_dados_rolados)):
        for i in range (7):
            if  i == lista_dados_rolados[a]:
                for chave, lista in dicionario.items():
                    if chave == i:
                        lista.append(i)
    for chave, lista in dicionario.items():
        if len(lista) >= 5:
            resultado = 50
    return resultado
# Questão 11
def calcula_pontos_regra_avancada  (lista_dados_rolados):
    dicionario = {}
    cinco_iguais = calcula_pontos_quina (lista_dados_rolados)
    full_house = calcula_pontos_full_house (lista_dados_rolados)
    quadra = calcula_pontos_quadra (lista_dados_rolados)
    sem_combinacao = calcula_pontos_soma (lista_dados_rolados)
    sequencia_alta = calcula_pontos_sequencia_alta (lista_dados_rolados)
    sequencia_baixa = calcula_pontos_sequencia_baixa (lista_dados_rolados)
    dicionario['cinco_iguais'] = cinco_iguais
    dicionario['full_house'] = full_house
    dicionario['quadra'] = quadra
    dicionario['sem_combinacao'] = sem_combinacao
    dicionario['sequencia_alta'] = sequencia_alta
    dicionario['sequencia_baixa'] = sequencia_baixa
    return dicionario
# Questão 12
def faz_jogada (lista_dados, categoria, cartela):
    for i in range (7):
        if categoria == f'{i}':
            categoria = i
    dicio_avancada = calcula_pontos_regra_avancada(lista_dados)
    dicio_simples = calcula_pontos_regra_simples(lista_dados)
    if categoria in dicio_simples:
        cartela['regra_simples'][categoria] = dicio_simples[categoria]
    if categoria in dicio_avancada:
        cartela['regra_avancada'][categoria] = dicio_avancada[categoria]
    return cartela
# Questão 13
def imprime_cartela(cartela) :
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)