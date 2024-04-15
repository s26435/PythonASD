def one_n_subsets(n):
    subsets = [[]]
    for i in range(1, n + 1):
        new_subsets = []
        for subset in subsets:
            max_el = max(subset) + 1 if subset else 1
            new_subsets.append(subset + [max_el])
        subsets.extend(new_subsets)
    return subsets


def next_subset(arr, n, k):
    i = k - 1
    while i >= 0 and arr[i] == n - k + i + 1:
        i -= 1
    if i < 0:
        return None
    arr[i] += 1
    for j in range(i + 1, k):
        arr[j] = arr[j - 1] + 1
    return arr


def k_subsets(n, k):
    if n <= k:
        raise ValueError("K nie może być większe od n!")
    subsets = [[]]
    subset = list(range(1, k + 1))
    while subset is not None:
        subsets.append(subset)
        subset = next_subset(subset, n, k)
    return subsets[1:]


def next_permutation(perm):
    n = len(perm)
    j = n - 2
    while j >= 0 and perm[j] >= perm[j + 1]:
        j -= 1
    if j == -1:
        return None
    k = n - 1
    while perm[k] <= perm[j]:
        k -= 1
    perm[j], perm[k] = perm[k], perm[j]
    perm[j + 1:] = reversed(perm[j + 1:])
    return perm


def permutations(n):
    apermutations = [[]]
    perm = list(range(1, n + 1))
    while perm is not None:
        apermutations.append(perm)
        perm = next_permutation(perm)
    return apermutations


def gray_code(n):
    if n <= 0:
        return ['']
    gray_code_lower = gray_code(n - 1)
    return ['0' + code for code in gray_code_lower] + ['1' + code for code in reversed(gray_code_lower)]


def gray_proc(n):
    result = [[]]
    arr = [0] * n
    i = 0
    while True:
        result.append(arr[::-1])
        i += 1
        p = 1
        j = i
        while j % 2 == 0:
            j //= 2
            p += 1
        if p <= n:
            arr[p - 1] = 1 - arr[p - 1]
        if p > n:
            break
    return result[1:]


def newton(n, k):
    if k < 0 or k > n:
        return 0
    result = 1
    for i in range(1, min(k, n - k) + 1):
        result *= n
        result //= i
        n -= 1
    return result


def generate_combinations_set_2(elements_set):
    combinations = []
    elements = list(elements_set)
    n = len(elements)
    for i in range(n):
        for j in range(i + 1, n):
            combinations.append((elements[i], elements[j]))
    return combinations


def print_pascals_triangle(rows):
    triangle = []
    for i in range(rows):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    width = len(' '.join(map(str, triangle[-1])))
    for row in triangle:
        print(' '.join(map(str, row)).center(width))


if __name__ == '__main__':
    print("ZADANIA\n-------------------------------------")
    # zad 1
    print("Wszystkie podzbiory {1...6}")
    print(one_n_subsets(6))
    # zad 2
    print("Wszystkie 3-elementowe podzbiory {1...6}")
    print(k_subsets(6, 3))
    # zad 3
    print("Wszystkie permutacje {1...6}")
    print(permutations(6))
    # zad 4
    print("liczby binarne Greya dla n = 6 rekurencyjnie")
    print(gray_code(6))
    print("liczby binarne Greya dla n = 6 proceduralnie")
    print(gray_proc(6))
    # zad 7
    print("kombinacje 2 elementowe z {1...7}")
    print(k_subsets(7, 2))
    print("kombinacje 2 elementowe z  {a,d,b,h,r,z,p}")
    print(generate_combinations_set_2({'a', 'd', 'b', 'h', 'r', 'z', 'p'}))
    print("PYTANIA\n ------------------------------------")
    # Ile różnych par studentów można utworzyć jeśli na roku jest 7 studentów?
    print(f"Z 7 studentów można utworzyć {newton(7, 2)} par.")
    # Ile różnych grup pięcioosobowych można utworzyć z 7 studentów ?
    print(f"Z 7 studentów można utworzyć {newton(7, 5)} grup 5osobowych.")
    # Wypisz wzór na (n nad k) upraszczając ułamek (załóż k<=n/2).
    print("n nad k jest równe n nad n-k pod warunkiem, że k<=n/2")
    # Narysuj trójkąt Pascala
    print("Trójkąt paskala dal 10 wierszy:")
    print_pascals_triangle(10)

