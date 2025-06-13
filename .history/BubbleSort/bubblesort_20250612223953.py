def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1): ##this is the important inner loop
            if arr[j] > arr[j + 1]:
                #swap if eleements are in wrong orrder
                arr[j], arr[j + 1] = arr[j +1], arr[j] ##shortcut for swapping in python
    return arr           


numbers = [5,3,8,4,2]
sorted_sample = bubble_sort(numbers)
print(sorted_sample)

