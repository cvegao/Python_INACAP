import random


selection = list(range(1, 10))
random.shuffle(selection)
print("Original list:", selection)


def order_list(some_list):
    n = 0
    while n < len(some_list):
        min_ = some_list[n]
        min_index = n
        for i in range(n, len(some_list)):
            if some_list[i] < min_:
                min_ = some_list[i]
                min_index = i
        some_list.pop(min_index)
        some_list.insert(n, min_)
        n += 1
    return some_list


print("Ordered list", order_list(selection))
