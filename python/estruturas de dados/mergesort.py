import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide o array ao meio
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursivamente ordena as duas metades
    left = merge_sort(left)
    right = merge_sort(right)

    # Combina as duas metades ordenadas
    return merge(left, right)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result

def main():
    try:
        n = int(input("Digite o número de elementos no array: "))
        arr = []
        for i in range(n):
            element = int(input(f"Digite o elemento {i + 1}: "))
            arr.append(element)

        print("Array original:")
        print(arr)

        start_time = time.time()
        sorted_arr = merge_sort(arr)
        end_time = time.time()

        print("Array ordenado:")
        print(sorted_arr)

        elapsed_time = end_time - start_time
        print(f"Tempo de ordenação: {elapsed_time:.6f} segundos")

    except ValueError:
        print("Por favor, digite números inteiros válidos.")

if __name__ == "__main__":
    main()
