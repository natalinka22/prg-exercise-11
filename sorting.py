import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(numbers):
    values = list(numbers)
    n = len(values)

    i = 0
    while i < n:
        min_index = i
        j = i + 1

        while j < n:
            if values[j] < values[min_index]:
                min_index = j
            j = j + 1

        if min_index != i:
            values[i], values[min_index] = values[min_index], values[i]

        i = i + 1

    return values

def bubble_sort():