import operator
from bisect import bisect_left
from functools import reduce


class ListSmallSize(Exception):
    """ The list is smaller than the specified size """
    pass


def mul(lst: list) -> int:
    """ Function to get product of list items.

    Args:
        lst (list): list of integers to multiply.

    Returns:
        int: multiplication result.
    """
    return reduce(operator.mul, lst, 1)


def insert_to_sized_sorted_list(lst: list, x: int, max_size: int) -> bool:
    """ Function to insert new value to sorted list with fixed size.
    If size of lst less than max_size, or if x greatest then minimum
    value in x, then insert x into lst. Else do nothing.
    Important! Function edit input list

    Args:
        lst (list): list of integers.
        x (int): value to insert.
        max_size (int): max_size of input list

    Returns:
        bool: True, if the item was added
    """
    i = bisect_left(lst, x)
    if i or len(lst) < max_size:
        lst.insert(i, x)
        return True


def max_triple_mul(lst: list) -> int:
    """ Function to find max production of 3 values in the list.

    Args:
        lst (list): list of integers to multiply (min. 3 items).

    Returns:
        int: max value of multiplication of 3 integers in the lst.

    Raises:
        ListSmallSize: Size of input list less than 3.
    """

    # check size of input list
    if len(lst) < 3:
        raise ListSmallSize("Size of list must be > 2")

    # if list contains only 3 values
    if len(lst) == 3:
        return mul(lst)

    # lists for 3 positive and 2 negative numbers
    positive = []
    negative = []

    for x in lst:
        # try insert each number to the appropriate list
        if x >= 0:
            insert_to_sized_sorted_list(positive, x, 3)
        else:
            insert_to_sized_sorted_list(negative, x, 2)

    return max(mul(negative) * positive[-1], mul(positive[-3:]))
