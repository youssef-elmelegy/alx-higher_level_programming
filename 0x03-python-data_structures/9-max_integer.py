#!/usr/bin/python3

def max_integer(my_list=[]):
    maxy = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > maxy:
            maxy = my_list[i]
    return (maxy)
