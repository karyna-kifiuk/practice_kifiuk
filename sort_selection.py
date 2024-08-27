def custom_selection_sort(list):
    length = len(list)
    for i in range(length):
        min_idx = i
        for j in range(i + 1, length):
            if list[j] < list[min_idx]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]
    return list

original_list = [55, 89, 63, 7, 47]
sorted_list = custom_selection_sort(original_list)
print("Sorted list:", sorted_list)
