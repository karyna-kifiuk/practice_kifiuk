def quicksort(q_list):
    if len(q_list) < 2:
        return q_list
    else:
        pivot = q_list[0]
        less = [element for element in q_list[1:] if element <= pivot]
        greater = [element for element in list[1:] if element > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

original_list = [25, 69, 73, 87, 10, 15, 5, 14, 7, 6, 5, 19, 33]
sorted_numbers = quicksort(original_list)

print("A sorted string of numbers:", sorted_numbers)
