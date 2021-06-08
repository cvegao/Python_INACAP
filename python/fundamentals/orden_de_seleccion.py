import random


selection = list(range(1, 10))
random.shuffle(selection)
print("Original list:", selection)


def order_list(some_list):
    new_list = []
    while len(some_list) != 0:
        min_ = some_list[0]
        min_index = 0
        for i in range(0, len(some_list)):
            if some_list[i] < min_:
                min_ = some_list[i]
                min_index = i
        new_list.append(min_)
        some_list.pop(min_index)
    return new_list


print("Ordered list", order_list(selection))
