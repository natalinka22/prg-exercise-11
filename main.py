from sorting import bubble_sort, bubble_sort_visualized, random_numbers, selection_sort
from hodnoceni_studentu import HodnoceniStudentu


def demo_cil_3_sorting_in_python():
    print("\nCIL 3: SORTING IN PYTHON")

    print("\n3.1 sort() and sorted()")
    numbers_for_sort = [3, 8, 1, 2, 32]
    print("Before sort():", numbers_for_sort)
    numbers_for_sort.sort()
    print("After sort(): ", numbers_for_sort)

    numbers_for_sorted = [3, 8, 1, 2, 32]
    new_sorted_numbers = sorted(numbers_for_sorted)
    print("Original list:", numbers_for_sorted)
    print("sorted(list):", new_sorted_numbers)

    print("\n3.2 reverse argument")
    descending_numbers = sorted(numbers_for_sorted, reverse=True)
    print("Descending:", descending_numbers)

    print("\n3.3 key argument")
    words = ["MOO", "meeeoow", "woof", "BZZZZZZ"]
    words_by_length = sorted(words, key=len)
    words_case_insensitive = sorted(words, key=str.lower)
    print("Original words:         ", words)
    print("Sorted by length (key):", words_by_length)
    print("Sorted by str.lower:    ", words_case_insensitive)


def demo_hodnoceni_studentu():
    print("\nCIL 4/5: OOP - HODNOCENI STUDENTU")

    results = HodnoceniStudentu([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print(results)
    print("Pocet studentu:", results.count())

    index = 0
    while index < results.count():
        points = results.get_by_index(index)
        grade = results.get_grade(index)
        print(f"Student {index}: {points} points - {grade}")
        index = index + 1

    print("Indexy studentu se 100 body:", results.find(100))
    print("Serazene vysledky:", results.get_sorted())
    print("Puvodni data:", results.scores)

    print("Prumer:", round(results.average(), 2))
    print("Nejlepsi vysledek:", results.best())
    print("Nejhorsi vysledek:", results.worst())
    print("Pass rate:", round(results.pass_rate(), 3))

    print("find_sorted(91):", results.find_sorted(91))
    print("find_sorted(50):", results.find_sorted(50))
    print("find_sorted(77):", results.find_sorted(77))

    random_results = HodnoceniStudentu(random_numbers(30, 0, 100))
    print("\nNahodna skupina - pocet studentu:", random_results.count())
    print("Nahodna skupina - serazene vysledky:", random_results.get_sorted())
    HodnoceniStudentu(random_numbers(500, 0, 100)).plot_histogram()


def main():
    short_values = [5, 1, 4, 2, 8]
    short_selection_sorted = selection_sort(short_values)
    short_bubble_sorted = bubble_sort(short_values)

    print("Original short list:", short_values)
    print("Selection sorted:  ", short_selection_sorted)
    print("Bubble sorted:     ", short_bubble_sorted)

    random_values = random_numbers(20)
    random_selection_sorted = selection_sort(random_values)
    random_bubble_sorted = bubble_sort(random_values)

    print("\nOriginal random list:", random_values)
    print("Selection sorted:    ", random_selection_sorted)
    print("Bubble sorted:       ", random_bubble_sorted)


    visual_values = random_numbers(10)
    bubble_sort_visualized(visual_values)

    demo_cil_3_sorting_in_python()
    demo_hodnoceni_studentu()


if __name__ == "__main__":
    main()