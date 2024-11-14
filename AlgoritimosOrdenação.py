import random
import time

# ------------------------------------------------------------------------------------------
def bubblesort(array):
    tamanho = len(array)
    comparacoes = 0
    trocou = True
    while trocou:
        trocou = False
        for i in range(0, tamanho - 1):
            comparacoes += 1
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                trocou = True
    return array, comparacoes
# ------------------------------------------------------------------------------------------
def selectionSort(V):
    comparacoes = 0
    tam = len(V)
    for N in range(0, tam):
        menor = V[N]
        indice = N
        for i in range(N, tam):
            comparacoes += 1
            if V[i] < menor:
                menor = V[i]
                indice = i
        if menor != V[N]:
            V[N], V[indice] = V[indice], V[N]
    return V, comparacoes
# ------------------------------------------------------------------------------------------
def InsertionSort(V):
    comparacoes = 0
    TAM = len(V)
    for N in range(0, TAM):
        aux = V[N]
        J = N - 1
        while J >= 0 and aux < V[J]:
            comparacoes += 1
            V[J + 1] = V[J]
            J -= 1
        V[J + 1] = aux
    return V, comparacoes
# ------------------------------------------------------------------------------------------
def Merge(V, inicio, meio, fim):
    p1 = inicio
    p2 = meio + 1
    vetorAux = []
    comparacoes = 0

    # Comparando elementos dos dois subarrays
    while p1 <= meio and p2 <= fim:
        comparacoes += 1
        if V[p1] < V[p2]:
            vetorAux.append(V[p1])
            p1 += 1
        else:
            vetorAux.append(V[p2])
            p2 += 1

    # Adicionando os elementos restantes da primeira metade (se houver)
    vetorAux.extend(V[p1:meio + 1])
    
    # Adicionando os elementos restantes da segunda metade (se houver)
    vetorAux.extend(V[p2:fim + 1])
    
    # Copiando de volta para o array original
    V[inicio:fim + 1] = vetorAux
    
    return comparacoes

def MergeSort(V, inicio, fim):
    comparacoes = 0
    if inicio < fim:
        meio = (inicio + fim) // 2
        # Contando comparações nas chamadas recursivas e na mesclagem
        comparacoes += MergeSort(V, inicio, meio)[1]
        comparacoes += MergeSort(V, meio + 1, fim)[1]
        comparacoes += Merge(V, inicio, meio, fim)
    return V, comparacoes

# ------------------------------------------------------------------------------------------
def QuickSort(V):
    if len(V) <= 1:
        return V, 0
    else:
        pivot = V[0]
        less = [x for x in V[1:] if x <= pivot]
        greater = [x for x in V[1:] if x > pivot]
        sorted_less, comp_less = QuickSort(less)
        sorted_greater, comp_greater = QuickSort(greater)
        return sorted_less + [pivot] + sorted_greater, comp_less + comp_greater + len(V) - 1
# ------------------------------------------------------------------------------------------
def HEAPSORT(V):
    def MAXHEAPIFY(V, i, tamanhoHeap):
        L = 2 * i + 1
        R = 2 * i + 2
        MAIOR = i
        if L < tamanhoHeap and V[L] > V[i]:
            MAIOR = L
        if R < tamanhoHeap and V[R] > V[MAIOR]:
            MAIOR = R
        if MAIOR != i:
            V[i], V[MAIOR] = V[MAIOR], V[i]
            MAXHEAPIFY(V, MAIOR, tamanhoHeap)

    def BUILDMAXHEAP(V):
        tamanhoHeap = len(V)
        for i in range(tamanhoHeap // 2 - 1, -1, -1):
            MAXHEAPIFY(V, i, tamanhoHeap)

    tamanhoHeap = len(V)
    BUILDMAXHEAP(V)
    comparacoes = 0
    for i in range(tamanhoHeap - 1, 0, -1):
        V[0], V[i] = V[i], V[0]
        MAXHEAPIFY(V, 0, i)
        comparacoes += 1
    return V, comparacoes
# ------------------------------------------------------------------------------------------
def CocktailSort(V):
    n = len(V)
    troca = True
    inicio = 0
    fim = n-1
    comparacoes = 0
    while (troca==True):

        # Reseta o menu de trocas (pode ser verdadeira da ultima interação)
        troca = False

        # Faz o loop da direita pra esquerda igual ao bouble
        for i in range (inicio, fim):
            comparacoes = comparacoes + 1
            if (V[i] > V[i+1]) :
                V[i], V[i+1]= V[i+1], V[i]
                troca=True

        # Se nada se mexeu, então o Array esta ordenado
        if (troca==False):
            break

        # Caso contrario, reseta o troca para ser utilizado na prox etapa
        troca = False

        # Aumenta um no estagio final, pois foi ordenado
        fim = fim-1

        # Da esquerda pra direita fazendo a mesma coisa
        # Compara assim como no estagio anterior
        for i in range(fim-1, inicio-1,-1):
            comparacoes = comparacoes + 1
            if (V[i] > V[i+1]):
                V[i], V[i+1] = V[i+1], V[i]
                troca = True

        # Aumenta um no estagio inicial, 
        # porque o ultimo estagio pode ter sido movido para o menor numero mais a direita
        inicio = inicio+1
    return V, comparacoes
# ------------------------------------------------------------------------------------------

# ==========================================================================================
def gerar_vetor(n, modo):
    if modo == 'c':
        return list(range(1, n + 1))
        # Se o modo for C, quer dizer que é crescente e vai de 1 até N+1, sendo N o valor colocado na entrada
    elif modo == 'd':
        return list(range(n, 0, -1))
        # Se o modo for D, é decrescente, então vai de N que é o valor escolhido até 0, de -1 em -1
    elif modo == 'r':
        return [random.randint(0, 32000) for _ in range(n)]
        # Se o modo for R, vão ter N numeros aleatorios de 0 a 32000
    else:
        raise ValueError("Modo de geração inválido!")
        # Se for nenhuma das três letras, o terminal vai exibir esse aviso
# ==========================================================================================
def salvar_saida(nome_arquivo, resultados):
    with open(nome_arquivo, 'w') as f: # abro o arquivo para escrita
        for resultado in resultados:
            metodo, vetor_ordenado, comparacoes, tempo = resultado
            f.write(f"{metodo}\n")
            f.write(" ".join(map(str, vetor_ordenado)) + "\n") # a função map converte tudo para string para poder escrever no arquivo de saida
            f.write(f"Comparações: {comparacoes}\n")
            f.write(f"Tempo (ms): {tempo:.2f}\n\n")
# ==========================================================================================
def executar_algoritmo(algoritmo, vetor):
    # Executa o algoritmo de ordenação e mede o tempo e comparações
    vetor_copy = vetor.copy()
    
    # Esse perf_counter é uma função da biblioteca time que faz com que o tempo seja mais preciso
    inicio = time.perf_counter()
    
    # Executa o algoritmo de ordenação e define o numero de comparações
    vetor_ordenado, comparacoes = algoritmo(vetor_copy)
    
    fim = time.perf_counter()
    tempo_gasto = (fim - inicio) * 1000  # conversão para milissegundos
    return vetor_ordenado, comparacoes, tempo_gasto
# ==========================================================================================
def main(arquivo_entrada, arquivo_saida):
    try:
        with open(arquivo_entrada, 'r') as f:
            # Leitura do tamanho do vetor
            linha1 = f.readline().strip()
            print(f"Conteúdo da primeira linha (tamanho do vetor): '{linha1}'")
            n = int(linha1)
            
            # Leitura do modo de geração do vetor
            linha2 = f.readline().strip()
            print(f"Conteúdo da segunda linha (modo): '{linha2}'")
            modo = linha2
            
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_entrada}' não foi encontrado.") # teste de mesa para quando achar o arquivo
        return
# ==========================================================================================

    # Geração do vetor
    vetor = gerar_vetor(n, modo)

    # Lista para armazenar os resultados
    resultados = []

    # Bubble Sort
    vetor_ordenado, comparacoes, tempo_gasto = executar_algoritmo(bubblesort, vetor)
    resultados.append(("Bubble Sort", vetor_ordenado, comparacoes, tempo_gasto))
    
    # Heap Sort
    vetor_ordenado, comparacoes, tempo_gasto = executar_algoritmo(HEAPSORT, vetor)
    resultados.append(("Heap Sort", vetor_ordenado, comparacoes, tempo_gasto))
    
    # Insertion Sort
    vetor_ordenado, comparacoes, tempo_gasto = executar_algoritmo(InsertionSort, vetor)
    resultados.append(("Insertion Sort", vetor_ordenado, comparacoes, tempo_gasto))
    
    # Selection Sort
    vetor_ordenado, comparacoes, tempo_gasto = executar_algoritmo(selectionSort, vetor)
    resultados.append(("Selection Sort", vetor_ordenado, comparacoes, tempo_gasto))
    
    # Merge Sort
    vetor_ordenado, comparacoes, tempo_gasto = executar_algoritmo(lambda v: MergeSort(v, 0, len(v) - 1), vetor)
    resultados.append(("Merge Sort", vetor_ordenado, comparacoes, tempo_gasto))
    
    # Quick Sort
    vetor_ordenado, comparacoes, tempo_gasto = executar_algoritmo(QuickSort, vetor)
    resultados.append(("Quick Sort", vetor_ordenado, comparacoes, tempo_gasto))
    #Cocktail Sort
    vetor_ordenado, comparacoes, tempo_gasto = executar_algoritmo(CocktailSort, vetor)
    resultados.append(("Cocktail Sort", vetor_ordenado, comparacoes, tempo_gasto))

    # Salvar os resultados no arquivo de saída e teste para garantir que está correto
    salvar_saida(arquivo_saida, resultados)
    print("Processo concluído com sucesso.")

# Executo o programa, definindo o nome do arquivo de entrada e o de saída
main("entrada.txt", "saida.txt")
