from quicksort import quicksort

def two_sum(nums, target):
    arr = []
    for idx in range(len(nums)):
        num = nums[idx]
        arr.append((num, idx))

    # Ordenar a lista usando quicksort
    # Nota: quicksort deve ordenar as tuplas com base no primeiro elemento (o valor numérico)
    quicksort(arr)

    # Dois ponteiros para encontrar os dois números (left e right)
    left = 0
    right = len(arr) - 1

    while left < right:
        # Acessamos arr[índice][0] para pegar o valor do número
        soma_atual = arr[left][0] + arr[right][0]
        
        if soma_atual == target:
            # Se encontramos o alvo, retornamos os índices originais que estão na posição 1 da tupla
            return [arr[left][1], arr[right][1]]
        elif soma_atual < target:
            # Se a soma for menor que o alvo, precisamos de um número maior (avançamos o 'left')
            left += 1
        else:
            # Se a soma for maior que o alvo, precisamos de um número menor (recuamos o 'right')
            right -= 1

    return []  # Não deveria acontecer, conforme o enunciado sempre tem uma solução.


def test_two_sum():
    # Teste 1 - Caso clássico
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Teste 1: {result} - Esperado: [0, 1] ou [1, 0]")

    # Teste 2 - Números negativos
    nums = [-3, 4, 3, 90]
    target = 0
    result = two_sum(nums, target)
    print(f"Teste 2: {result} - Esperado: [0, 2] ou [2, 0]")

    # Teste 3 - Repetição de números
    nums = [3, 3]
    target = 6
    result = two_sum(nums, target)
    print(f"Teste 3: {result} - Esperado: [0, 1] ou [1, 0]")

    # Teste 4 - Números com zero
    nums = [0, 4, 3, 0]
    target = 0
    result = two_sum(nums, target)
    print(f"Teste 4: {result} - Esperado: [0, 3] ou [3, 0]")

    # Teste 5 - Target negativo
    nums = [-1, -2, -3, -4, -5]
    target = -8
    result = two_sum(nums, target)
    print(f"Teste 5: {result} - Esperado: [2, 4] ou [4, 2]")

    # Teste 6 - Target positivo, números mistos
    nums = [1, -2, 3, 5, -4, 8]
    target = 4
    result = two_sum(nums, target)
    print(f"Teste 6: {result} - Esperado: [0, 2] ou [2, 0] (depende da ordem)")

    # Teste 7 - Não existe par (não deve acontecer, mas importante testar)
    nums = [1, 2, 3]
    target = 10
    result = two_sum(nums, target)
    print(f"Teste 7: {result} - Esperado: []")

    # Teste 8 - Par é o menor e maior elemento
    nums = [1, 5, 10, 20, 50]
    target = 51
    result = two_sum(nums, target)
    print(f"Teste 8: {result} - Esperado: [0, 4] ou [4, 0]")

    # Teste 9 - Par adjacente
    nums = [1, 2, 3, 4, 5]
    target = 7
    result = two_sum(nums, target)
    print(f"Teste 9: {result} - Esperado: [2, 3] ou [3, 2]") # Nota: arrumado no comentário de expectativa, 3+4=7, que são os índices 2 e 3 originais.

    # Teste 10 - Par nos extremos (com valores iguais)
    nums = [5, 1, 2, 3, 5]
    target = 10
    result = two_sum(nums, target)
    print(f"Teste 10: {result} - Esperado: [0, 4] ou [4, 0]")

# Nota: Para rodar este código, certifique-se de ter um arquivo 'quicksort.py' no mesmo diretório 
# contendo a implementação da função quicksort, ou substitua 'quicksort(arr)' por 'arr.sort()'.
# test_two_sum()
