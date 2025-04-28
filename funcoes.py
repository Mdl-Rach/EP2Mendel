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
