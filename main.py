from sorting import bubble_sort, bubble_sort_visualized, random_numbers, selection_sort


def main():
    short_values = [5, 1, 4, 2, 8]
    short_sorted = selection_sort(short_values)
    short_bubble_sorted = bubble_sort(short_values)

    print("Original short list:", short_values)
    print("Sorted short list:  ", short_sorted)
    print("Bubble sorted:     ", short_bubble_sorted)

    random_values = random_numbers(20)
    random_selection_sorted = selection_sort(random_values)
    random_bubble_sorted = bubble_sort(random_values)

    print("\nOriginal random list:", random_values)
    print("Selection sorted:    ", random_selection_sorted)
    print("Bubble sorted:       ", random_bubble_sorted)

    visual_values = random_numbers(10)
    bubble_sort_visualized(visual_values)

if __name__ == "__main__":
    main()