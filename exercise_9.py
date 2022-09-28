list1 = [1, 2, 3, 4, 5]
list2 = [1, 3, 4]


def cleaner(lst, clean_items):
    for i in clean_items:
        for x in lst:
            if x == i:
                lst.remove(x)


cleaner(list1, list2)
print(list1)
