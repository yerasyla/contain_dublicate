def contain_dublicates(some_list):

    return len(some_list) != len(set(some_list))

list = [1, 3, 5, 1]
print(contain_dublicates(list))