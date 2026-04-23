import random
import matplotlib.pyplot as plt

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


def bubble_sort(numbers):
    values = list(numbers)
    n = len(values)

    i = 0
    while i < n:
        swapped = False
        j = 0

        while j < (n - 1 - i):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True
            j = j + 1

        if swapped is False:
            break

        i = i + 1

    return values


def bubble_sort_visualized(numbers, pause_seconds=0.1):
    values = list(numbers)
    n = len(values)

    plt.ion()
    plt.show()

    i = 0
    while i < n:
        swapped = False
        j = 0

        while j < (n - 1 - i):
            index_highlight1 = j
            index_highlight2 = j + 1

            colors = []
            color_index = 0
            while color_index < len(values):
                colors.append('steelblue')
                color_index = color_index + 1

            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"

            plt.clf()
            plt.bar(range(len(values)), values, color=colors)
            plt.title("Bubble Sort")
            plt.pause(pause_seconds)

            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True

            j = j + 1

        if swapped is False:
            break

        i = i + 1

    plt.ioff()
    plt.show()

    return values




