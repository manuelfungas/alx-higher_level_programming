#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_set = set(my_list)
    for num in uniq_set:
        if num not in uniq_set:
            uniq_set.add(num)
    return sum(uniq_set)
