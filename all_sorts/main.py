import random
from datetime import datetime


def standart_sort(array):
    start_time = datetime.now()
    sort_array = sorted(array)
    end_time = datetime.now()
    time_program = end_time - start_time
    print(f'Duration standart_sort: {time_program}')
    return sort_array


def bubble_sort(array):
    start_time = datetime.now()
    for j in range(len(array) - 1):
        for i in range(1, len(array) - j):
            if array[i - 1] > array[i]:
                temp = array[i - 1]
                array[i - 1] = array[i]
                array[i] = temp
    end_time = datetime.now()
    time_program = end_time - start_time
    print(f'Duration bubble_sort: {time_program}')
    return array


def selection_sort(array):
    start_time = datetime.now()
    for i in range(len(array)):
        min_elem = 49857982379872
        for j in range(i, len(array)):
            if array[j] < min_elem:
                min_elem = array[j]
        array[i] = min_elem
    end_time = datetime.now()
    time_program = end_time - start_time
    print(f'Duration selection_sort: {time_program}')
    return array


def cocktail_sort(array):
    start_time = datetime.now()
    for j in range(len(array) // 2 + 1):
        for i in range(1, len(array) - j):
            #if j % 2 == 0:
                temp = array[i - 1]
                if temp > array[i]:
                    array[i - 1] = array[i]
                    array[i] = temp
            #else:
                temp = array[- i]
                if temp < array[-1 - i]:
                    array[-1 - i] = array[-i]
                    array[-i] = temp
    end_time = datetime.now()
    time_program = end_time - start_time
    print(f'Duration cocktail_sort: {time_program}')
    return array


def insertion_sort(array):
    start_time = datetime.now()
    count = 0
    for i in range(1, len(array)):
        if array[i - 1] <= array[i]:
            continue
        else:
            count = i
            break
    for i in range(count, len(array) - 1):
        for j in range(i, len(array)):
            while array[j] < array[j - 1] and j > 0:
                temp = array[j - 1]
                array[j - 1] = array[j]
                array[j] = temp
    end_time = datetime.now()
    time_program = end_time - start_time
    print(f'Duration insertion_sort: {time_program}')
    return array


def merge(array, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    left_array = [0 for _ in range(n1)]
    right_array = [0 for _ in range(n2)]

    for i in range(0, n1):
        left_array[i] = array[l + i]

    for j in range(0, n2):
        right_array[j] = array[m + 1 + j]

    i = 0
    j = 0
    temp = l

    while i < n1 and j < n2:
        if left_array[i] <= right_array[j]:
            array[temp] = left_array[i]
            i += 1
        else:
            array[temp] = right_array[j]
            j += 1
        temp += 1

    while i < n1:
        array[temp] = left_array[i]
        i += 1
        temp += 1

    while j < n2:
        array[temp] = right_array[j]
        j += 1
        temp += 1


def merge_sort(array, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(array, l, m)
        merge_sort(array, m + 1, r)
        merge(array, l, m, r)
    return array


def heapify(array, n, i):
    largest = i
    l = 2 * i + 1   # left = 2*i + 1
    r = 2 * i + 2   # right = 2*i + 2

    if l < n and array[i] < array[l]:
        largest = l

    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        temp = array[largest]
        array[largest] = array[i]
        array[i] = temp

        heapify(array, n, largest)


def heap_sort(array):
    start_time = datetime.now()
    n = len(array)

    for i in range(n, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        temp = array[i]
        array[i] = array[0]
        array[0] = temp
        heapify(array, i, 0)
    end_time = datetime.now()
    time_program = end_time - start_time
    print(f'Duration heap_sort: {time_program}')
    return array


def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        q = random.choice(array)
    l_nums = [n for n in array if n < q]

    e_nums = [q for _ in range(array.count(q))]
    b_nums = [n for n in array if n > q]
    return quick_sort(l_nums) + e_nums + quick_sort(b_nums)


minrun = 32



def InsSort(arr, start, end):
    for i in range(start + 1, end + 1):
        elem = arr[i]
        j = i - 1
        while j >= start and elem < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = elem
    return arr


def merge(arr, start, mid, end):
    if mid == end:
        return arr
    first = arr[start:mid + 1]
    last = arr[mid + 1:end + 1]
    len1 = mid - start + 1
    len2 = end - mid
    ind1 = 0
    ind2 = 0
    ind = start

    while ind1 < len1 and ind2 < len2:
        if first[ind1] < last[ind2]:
            arr[ind] = first[ind1]
            ind1 += 1
        else:
            arr[ind] = last[ind2]
            ind2 += 1
        ind += 1

    while ind1 < len1:
        arr[ind] = first[ind1]
        ind1 += 1
        ind += 1

    while ind2 < len2:
        arr[ind] = last[ind2]
        ind2 += 1
        ind += 1

    return arr


def Tim_sort(array):
    start_time = datetime.now()
    n = len(array)

    for start in range(0, n, minrun):
        end = min(start + minrun - 1, n - 1)
        array = InsSort(array, start, end)

    curr_size = minrun
    while curr_size < n:
        for start in range(0, n, curr_size * 2):
            mid = min(n - 1, start + curr_size - 1)
            end = min(n - 1, mid + curr_size)
            array = merge(array, start, mid, end)
        curr_size *= 2
    end_time = datetime.now()
    time_program = end_time - start_time
    print(f'Duration Tim_sort: {time_program}')
    return array


my_array = [random.randint(0, 100) for i in range(10000)]


print(standart_sort(my_array))
print(bubble_sort(my_array))
print(selection_sort(my_array))
print(cocktail_sort(my_array))
print(insertion_sort(my_array))

le = random.randint(0, 100)
ri = random.randint(0, 100)
start_time = datetime.now()
print(merge_sort(my_array, le, ri))
end_time = datetime.now()
time_program = end_time - start_time
print(f'Duration merge_sort: {time_program}')

print(heap_sort(my_array))

start_time = datetime.now()
print(quick_sort(my_array))
end_time = datetime.now()
time_program = end_time - start_time
print(f'Duration quick_sort: {time_program}')

print(Tim_sort(my_array))
