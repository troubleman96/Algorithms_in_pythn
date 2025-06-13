def selection_sort(arr):
    for i in range(0, len(arr) -1): ##the legngthof array minus one since idenx is zero
        cur_min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[cur_min_index]: ##if the current element is less than the minimum element found so far
                cur_min_index = j
        #swap the current element with the minimum element found
        arr[i], arr[cur_min_index] = arr[cur_min_index], arr[i]  ##the python schortcut for swapping

arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array is:", arr)  ##print the sorted array