import random
import time

def defaultProgram(l, tamanho, alvo):
  inicio = time.time()
  contador = 0
  # Geração da lista de números únicos
  while len(l) < tamanho:
    num = random.randint(0, valor_maximo)
    if num not in l:
      l.append(num)

  # Cálculo de pares cuja soma é igual ao alvo
  for i in l:
    compl = alvo - i
    if compl in l:
      contador += 1

  # Resultado ajustado para não contar pares duplicados e tempo de execução
  tempo_decorrido = time.time() - inicio
  print('Função Default ----------------------------------')
  print(f"Tempo de execução: {tempo_decorrido} segundos")
  print(f"Há {int(contador/2)} pares cuja a soma é igual a {alvo}")
  print()

def mergeSortAndDefault(l, tamanho, alvo):
  inicio = time.time()

  # Resultado ajustado para não contar pares duplicados e tempo de execução
  tempo_decorrido = time.time() - inicio
  print('Função Merge Sort + Processo Default ----------------------------------')
  print(f"Tempo de execução: {tempo_decorrido} segundos")
  print(f"Há {int(contador/2)} pares cuja a soma é igual a {alvo}")
  print()

def paresPorConjunto(l, alvo):
  inicio = time.time()
  visto = set()
  pares = set()
  
  for numero in l:
    complemento = alvo - numero
    if complemento in visto:
      pares.add((min(numero, complemento), max(numero, complemento)))
    visto.add(numero)

  
  tempo_decorrido = time.time() - inicio
  print('Função Pares por Conjunto ----------------------------------')
  print(f"Tempo de execução: {tempo_decorrido} segundos")
  print(f"Há {len(pares)} pares cuja a soma é igual a {alvo}")
  print()

def paresPonteiros(l, tamanho, alvo):
  inicio = time.time()
  l.sort()
  esquerda, direita = 0, tamanho - 1
  pares = []
  while esquerda < direita:
    soma_atual = l[esquerda] + l[direita]
    if soma_atual == alvo:
      pares.append((l[esquerda], l[direita]))
      esquerda += 1 
      direita -= 1
    elif soma_atual < alvo:
      esquerda += 1
    else:
      direita -= 1
  tempo_decorrido = time.time() - inicio
  print('Função Pares Ponteiros ----------------------------------')
  print(f"Tempo de execução: {tempo_decorrido} segundos")
  print(f"Há {len(pares)} pares cuja a soma é igual a {alvo}")
  print()

# Começo do programa
valor_maximo = random.randint(0, 2**17)
tamanho = int(input("Digite o tamanho do array: "))

random.seed(tamanho)
l = []

# Seleção de um alvo ímpar
alvo = random.randint(0, valor_maximo)
while alvo % 2 == 0:
  alvo = random.randint(0, valor_maximo)

# defaultProgram(l, tamanho, alvo)
mergeSortAndDefault(l, tamanho, alvo)
paresPorConjunto(l,alvo)
paresPonteiros(l, tamanho, alvo)


