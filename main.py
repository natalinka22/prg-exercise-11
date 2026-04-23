from sorting import random_numbers, selection_sort


def main():
    short_values = [5, 1, 4, 2, 8]
    short_sorted = selection_sort(short_values)

    print("Original short list:", short_values)
    print("Sorted short list:  ", short_sorted)

    random_values = random_numbers(20)
    random_sorted = selection_sort(random_values)

    print("\nOriginal random list:", random_values)
    print("Sorted random list:  ", random_sorted)


if __name__ == "__main__":
    main()