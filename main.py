import sys
import os
from random import randrange
from timeit import default_timer as timer
sys.setrecursionlimit(3600)
import random

#Variaveis Globais para Teste de Complexidade dos métodos Quick e Merge
compBubble = 0
compSelection = 0
compInsertion = 0
compMerge = 0
compQuick = 0

def calcula_tempo(vet, func):
	n = len(vet)
	start = timer()
	func(vet)
	end = timer()
	print(f"{func.__name__}: {end - start:.5f} segundos")
	if func.__name__ == "bubbleSort":
		print(f"Tamanho do Vetor: {n} - Complexidade: {compBubble}\n")
	elif func.__name__ == "selectionSort":
		print(f"Tamanho do Vetor: {n} - Complexidade: {compSelection}\n")
	elif func.__name__ == "insertionSort":
		print(f"Tamanho do Vetor: {n} - Complexidade: {compInsertion}\n")
	elif func.__name__ == "mergeSort":
		print(f"Tamanho do Vetor: {n} - Complexidade: {compMerge}\n")
	elif func.__name__ == "quickSort":
		print(f"Tamanho do Vetor: {n} - Complexidade: {compQuick}\n")
	
def bubbleSort(vet):
	global compBubble
	ordenado = False
	compBubble = 0
	n = len(vet) - 1
	
	while not ordenado:
		ordenado = True
		for i in range(n):
			if (vet[i] > vet[i+1]):
				vet[i], vet[i+1] = vet[i+1], vet[i]
				ordenado = False
			compBubble += 1
		compBubble += 1

def selectionSort(vet):
	global compSelection
	comp = 0
	n = len(vet) - 1
	
	for i in range(n):
		menor = i
		for j in range(i + 1, n):
			if (vet[j] < vet[menor]):
				menor = j
			compSelection += 1
		vet[i], vet[menor] = vet[menor], vet[i]
		compSelection += 1

def insertionSort(vet):
	global compInsertion
	
	for i in range(1, len(vet)):
		key = vet[i]
		j = i-1
		while j >=0 and key < vet[j] :
			vet[j+1] = vet[j]
			j -= 1
			compInsertion += 1
		vet[j+1] = key
		compInsertion += 1
	
def mergeSort(vet):
	global compMerge
	compMerge += 1
	
	if len(vet) > 1:
		meio = len(vet) // 2
		esquerda = vet[:meio]
		direita = vet[meio:]
		
		mergeSort(esquerda)
		mergeSort(direita)
		
		i = j = k = 0
		
		while i < len(esquerda) and j < len(direita):
			if esquerda[i] <= direita[j]:
				vet[k] = esquerda[i]
				i += 1
			else:
				vet[k] = direita[j]
				j += 1
			k += 1
			compMerge += 1
		while i < len(esquerda):
			vet[k] = esquerda[i]
			i += 1
			k += 1
			compMerge += 1
		while j < len(direita):
			vet[k] = direita[j]
			j += 1
			k += 1
			compMerge += 1

def quickSort(vet, primeiro=0, ultimo=None):
	global compQuick
	compQuick += 1
	
	if ultimo is None:
		ultimo = len(vet) - 1

	if primeiro >= ultimo: return
	
	i, j = primeiro, ultimo
	pivo = vet[random.randint(primeiro, ultimo)]
	
	while i <= j:
		while vet[i] < pivo:
			i += 1
			compQuick += 1
		while vet[j] > pivo:
			j -= 1
			compQuick += 1
		if i <= j:
			vet[i], vet[j] = vet[j], vet[i]
			i, j = i + 1, j - 1
		compQuick += 1
	quickSort(vet, primeiro, j)
	quickSort(vet, i, ultimo)

def criar_bd_desordenado(tamanhoVetor, faixaNumeros):
	with open(f"bd_desordenado - {tamanhoVetor}.txt", "w+") as arq: # GERA O ARQUIVO
		for i in range(tamanhoVetor):
			valor = randrange(0,faixaNumeros)
			arq.write(str(valor)+'\n') #Valor a ser armazenado no arquivo
	print("Criar BD Desordenado concluido!")

def criar_bd_ordenado_crescente(tamanhoVetor):
	with open(f"bd_desordenado - {tamanhoVetor}.txt", "r+") as arq:
		c = arq.read()
		v = c.split('\n')
		vetor = [int(elem) for elem in v if elem != '']
		
	with open(f"bd_ordenado_crescente - {tamanhoVetor}.txt", "w+") as arq: # GERA O ARQUIVO
		vetor.sort()
		for i in vetor:
			arq.write(str(i)+'\n') #Valor a ser armazenado no arquivo
	print("Criar BD ordenado crescente concluido")

def criar_bd_ordenado_decrescente(tamanhoVetor):
	with open(f"bd_desordenado - {tamanhoVetor}.txt", "r+") as arq:
		c = arq.read()
		v = c.split('\n')
		vetor = [int(elem) for elem in v if elem != '']

	with open(f"bd_ordenado_decrescente - {tamanhoVetor}.txt", "w+") as arq: # GERA O ARQUIVO
		vetor.sort(reverse=True)
		for i in vetor:
			arq.write(str(i)+'\n') #Valor a ser armazenado no arquivo
	print("Criar BD ordenado decrescente concluido")

def ler_bd(nomeBD):
	with open(nomeBD+".txt", "r+") as arq:
		c = arq.read()
		v = c.split('\n')
		vetor = [int(elem) for elem in v if elem != '']
	return vetor

def main():
	while True:
		compBubble = compSelection = compInsertion = 0
		compMerge = compQuick = 0
		os.system("CLS")
		print("\n1: Ord. Crescente \n2: Desordenado \n3: Ord.Decrescente")
		opcaoOrdenacao = int(input("Qual tipo de vetor: "))
		if opcaoOrdenacao < 1 or opcaoOrdenacao > 3:
			print("Progrema Parado")
			break

		print("\n# 1 - 1000")
		print("# 2 - 10000")
		print("# 3 - 100000")
		print("# 4 - 1000000")
		print("# 5 - 2000000")
		tam_vetor = int(input("Escolha tamanho do Vetor: "))
		if tam_vetor < 1 or tam_vetor > 5:
			print("Progrema Parado")
			break
		elif tam_vetor == 1:
			n = 1000
		elif tam_vetor == 2:
			n = 10000
		elif tam_vetor == 3:
			n = 100000
		elif tam_vetor == 4:
			n = 1000000
		elif tam_vetor == 5:
			n = 2000000
		
		bd_desordenado = f"bd_desordenado - {n}"
		bd_ordenado_crescente = f"bd_ordenado_crescente - {n}"
		bd_ordenado_decrescente = f"bd_ordenado_decrescente - {n}"
		
		if opcaoOrdenacao == 1:
			ordenacao = ler_bd(bd_ordenado_crescente)
		elif opcaoOrdenacao == 2:
			ordenacao = ler_bd(bd_desordenado)
		elif opcaoOrdenacao == 3:
			ordenacao = ler_bd(bd_ordenado_decrescente)
			
		print("\n# 1 - Bubble Sort")
		print("# 2 - Selection Sort")
		print("# 3 - Insertion Sort")
		print("# 4 - Merge Sort")
		print("# 5 - Quick Sort")
		print("# 6 - Todos")
		metodo = int(input("Digite o método escolhido: "))
		print("")
		if metodo < 0:
			print("Progrema Parado")
			break
		elif metodo == 1:
			calcula_tempo(ordenacao, bubbleSort)
		elif metodo == 2:
			calcula_tempo(ordenacao, selectionSort)
		elif metodo == 3:
			calcula_tempo(ordenacao, insertionSort)
		elif metodo == 4:
			calcula_tempo(ordenacao, mergeSort)
		elif metodo == 5:
			calcula_tempo(ordenacao, quickSort)
		elif metodo == 6:
			calcula_tempo(ordenacao, bubbleSort)
			calcula_tempo(ordenacao, selectionSort)
			calcula_tempo(ordenacao, insertionSort)
			calcula_tempo(ordenacao, mergeSort)
			calcula_tempo(ordenacao, quickSort)
		del ordenacao
		os.system("PAUSE")
		
if __name__ == "__main__":
	main()
"""
	tamanhos = [1000, 10000, 100000, 1000000, 2000000]
	tamanho = tamanhos[2]
	quatidade_string = f'{tamanho}'
	bd_desordenado = f"bd_desordenado - {tamanho}"
	bd_ordenado_crescente = f"bd_ordenado_crescente - {tamanho}"
	bd_ordenado_decrescente = f"bd_ordenado_decrescente - {tamanho}"
	
	# FUNÇÕES PARA CRIAR BDS
	#criar_bd_desordenado(quantidade, 1000)
	#criar_bd_ordenado_crescente(quantidade)
	#criar_bd_ordenado_decrescente(quantidade)

	for i in range(3):
		compBubble = 0
		compSelection = 0
		compInsertion = 0
		compMerge = 0
		compQuick = 0
		
		# FUNÇÕES PARA LER BDS
		#ordenacao = ler_bd(bd_desordenado)
		#ordenacao = ler_bd(bd_ordenado_crescente)
		ordenacao = ler_bd(bd_ordenado_decrescente)
		
		calcula_tempo(ordenacao, bubbleSort)
		#calcula_tempo(ordenacao, selectionSort)
		#calcula_tempo(ordenacao, insertionSort)
		del ordenacao
"""
