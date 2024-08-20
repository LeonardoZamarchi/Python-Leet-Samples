from timeit import timeit

def constante(arr,pos):
    print('constante O(1)')
    if pos <= len(arr) - 1:
        return arr[pos]

def linear(arr):
    print('Linear O(n)')
    for n in arr:
        print(n)

#só retorna a posição correta se a lista estiver ordenada
def logaritmico(arr,target):
    print('logaritmico O(log n)')
    arr = sorted(arr)
    left, right = 0, len(arr)-1
    while left <= right:
        mid = left + (right-left) // 2
        if arr[mid] == target:
            return 'Pos Target: '+ str(mid)
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid-1
    
    return -1

def linearitmico(arr):
    print('linearitmico/merge_sort O(n log n)')
    if len(arr)>1:
        mid = len(arr) //2
        left_half = arr[:mid]
        right_half = arr[:mid]
        linearitmico(left_half)
        linearitmico(right_half)
        merge(arr, left_half, right_half)

def merge(arr, left, right):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    # Copia os elementos restantes das metades esquerda e direita
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def quadratico(arr):
    print('quadratico/bubble_sort O(n2)')
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


sample_arr = [38, 27, 43, 3, 9, 82, 10, 30, 73, 99]
index = 5
target = 82
print(f'Entrada: {sample_arr}')
print(f'Index: {index}')
print(f'Target: {target}')
print(constante(sample_arr, index))
linear(sample_arr)
print(logaritmico(sample_arr,target))
print(linearitmico(sample_arr))
print(quadratico(sample_arr))
