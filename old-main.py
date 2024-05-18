import random
import time

valor_maximo = random.randint(0, 2**17)
tamanho = int(input())

inicio = time.time()

random.seed(tamanho)
l = []

# Geração da lista de números únicos
while len(l) < tamanho:
  num = random.randint(0, valor_maximo)
  if num not in l:
    l.append(num)

# Seleção de um alvo ímpar
alvo = random.randint(0, valor_maximo)
while alvo % 2 == 0:
  alvo = random.randint(0, valor_maximo)

contador = 0

# Cálculo de pares cuja soma é igual ao alvo
for i in l:
  compl = alvo - i
  if compl in l:
    contador += 1

# Resultado ajustado para não contar pares duplicados e tempo de execução
tempo_decorrido = time.time() - inicio
print(f"Tempo de execução: {tempo_decorrido} segundos")
print(int(contador/2))