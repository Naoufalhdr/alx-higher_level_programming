#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """ Deletes keys with a specific value in a dictionary. """
    del_keys = [k for k, v in a_dictionary.items() if v == value]
    for key in deleted_keys:
        del a_dictionary[key]
    return (a_dictionary)

