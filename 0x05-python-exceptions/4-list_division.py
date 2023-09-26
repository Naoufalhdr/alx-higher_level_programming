#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    i = 0
    new_list = []
    while i < list_length:
        try:
            result = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            result = 0
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        i += 1
        new_list.append(result)
    return new_list
