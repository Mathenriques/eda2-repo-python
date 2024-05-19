import random
import time


def algoritimo_padrao(alvo, tamanho, valor_maximo):
    inicio = time.time()

    # Geração da lista de números únicos
    lista = []
    while len(lista) < int(tamanho):
        num = random.randint(0, valor_maximo)
        if num not in lista:
            lista.append(num)
    contador = 0

    # Cálculo de pares cuja soma é igual ao alvo
    for i in lista:
        compl = alvo - i
        if compl in lista:
            contador += 1

    # Resultado ajustado para não contar pares duplicados e tempo de execução
    tempo_decorrido = time.time() - inicio
    print(f"Tempo de execução da função padrão: {tempo_decorrido} segundos")
    print(f"Pares encontrados {int(contador / 2)}")


def algoritimo_padrao_hash_generate(alvo, tamanho, valor_maximo):
    inicio = time.time()

    # Geração da lista de números únicos
    lista = []
    numeros_gerados = set()
    while len(lista) < int(tamanho):
        num = random.randint(0, valor_maximo)
        if num not in numeros_gerados:
            lista.append(num)
    contador = 0

    # Cálculo de pares cuja soma é igual ao alvo
    for i in lista:
        compl = alvo - i
        if compl in lista:
            contador += 1

    # Resultado ajustado para não contar pares duplicados e tempo de execução
    tempo_decorrido = time.time() - inicio
    print(f"Tempo de execução da função padrão com generated hash: {tempo_decorrido} segundos")
    print(f"Pares encontrados {int(contador / 2)}")


def hastable_algoritmo(alvo, tamanho, valor_maximo):
    inicio = time.time()
    visto = set()
    pares = set()

    # Geração da lista de números únicos
    lista = []
    numeros_gerados = set()
    while len(lista) < int(tamanho):
        num = random.randint(0, valor_maximo)
        if num not in numeros_gerados:
            lista.append(num)

    for numero in lista:
        complemento = alvo - numero
        if complemento in visto:
            pares.add((min(numero, complemento), max(numero, complemento)))
        visto.add(numero)

    tempo_decorrido = time.time() - inicio
    print(f"Tempo de execução da função com tabela hash: {tempo_decorrido} segundos")
    print(f"Pares encontrados {len(pares)}")


def pointeiros_pares(alvo, tamanho, valor_maximo):
    inicio = time.time()

    # Geração da Lista de Itens
    lista = []
    numeros_gerados = set()
    while len(lista) < int(tamanho):
        num = random.randint(0, valor_maximo)
        if num not in numeros_gerados:
            lista.append(num)

    # Antes da execução é necessário a ordenação:
    lista.sort()
    # Definição dos Ponteiros
    esquerda = 0
    direita = len(lista) - 1

    # Definição da lista de pares (hash)
    pares = set()

    while esquerda < direita:
        soma_atual = lista[esquerda] + lista[direita]
        if soma_atual == alvo:
            pares.add((lista[esquerda], lista[direita]))
            esquerda += 1
            direita -= 1
        elif soma_atual < alvo:
            esquerda += 1
        else:
            direita -= 1

    tempo_decorrido = time.time() - inicio
    print(f"Tempo de execução da função com tabela pointeiros pares: {tempo_decorrido} segundos")
    print(f"Pares encontrados {len(pares)}")


# Inicio do programa
valor_maximo = random.randint(0, 2**17)
tamanho = input("Qual o tamanho da lista? ")

random.seed(tamanho)

# Seleção de um alvo ímpar
alvo = random.randint(0, valor_maximo)
while alvo % 2 == 0:
    alvo = random.randint(0, valor_maximo)


algoritimo_padrao(alvo, tamanho, valor_maximo)
algoritimo_padrao_hash_generate(alvo, tamanho, valor_maximo)
hastable_algoritmo(alvo, tamanho, valor_maximo)
pointeiros_pares(alvo, tamanho, valor_maximo)
