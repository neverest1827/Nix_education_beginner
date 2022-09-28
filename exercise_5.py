myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
          18, 19, 20]
count = int(input('>'))


def list_shredder(input, size):
    input_size = len(input)
    slice_size = int(input_size / size)
    remain = input_size % size
    result = []
    iterator = iter(input)
    if input_size < size:
        print('''Некоректрый запрос: число элементов списка
меньше чем число деления''')
    else:
        for i in range(size):
            result.append([])
            for j in range(slice_size):
                result[i].append(iterator.__next__())
            if remain:
                result[i].append(iterator.__next__())
                remain -= 1
        print(result)



list_shredder(myList, count)
