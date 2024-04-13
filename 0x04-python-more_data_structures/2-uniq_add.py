#!/usr/bin/python3
def uniq_add(my_list=[]):
    UniqList = set()
    if my_list:
        for i in my_list:
            UniqList.add(i)
    return sum(UniqList)
