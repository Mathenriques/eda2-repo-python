import random
import time
def algoritimopadrao(alvo, tamanho, valor_maximo):
    inicio = time.time()
    # Geração da lista de números únicos
    lista = []
    while len(lista) < tamanho:
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


valor_maximo = random.randint(0, 2**17)
tamanho = int(input())

random.seed(tamanho)

# Seleção de um alvo ímpar
alvo = random.randint(0, valor_maximo)
while alvo % 2 == 0:
    alvo = random.randint(0, valor_maximo)


algoritimopadrao(alvo, tamanho, valor_maximo)