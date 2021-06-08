import random


selection = list(range(1, 10))
random.shuffle(selection)
print("Original list:", selection)


def order_list(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if arr[i] < arr[j]:
                arr[j], arr[i] = arr[i], arr[j]

    return arr
