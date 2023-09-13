#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """ Deletes keys with a specific value in a dictionary. """
    """
    del_keys = [k for k, v in a_dictionary.items() if v == value]
    """
    deleted_keys = []
    for key, key_value in a_dictionary.items():
        if key_value is value:
            deleted_keys.append(key)
    for x in deleted_keys:
        del a_dictionary[x]
    return a_dictionary

