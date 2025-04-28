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
