#!/usr/bin/python3
""" Module define peak function """


def find_peak(list_of_integers):
    """
    Function to find a peak in a list of unsorted integers.

    Args:
        list_of_integers: List of unsorted integers.

    Returns:
        A peak element from the list.

    Complexity:
        O(log(n)), where n is the number of elements in the list.
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
