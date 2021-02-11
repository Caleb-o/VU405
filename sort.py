"""
    Author:     Caleb Otto-Hayes
    Date:      11/2/2021
"""

def swap(x: int, y: int) -> tuple:
    return (y, x)

def bubbleSort(unsorted: list) -> None:
    length: int = len(unsorted)
    full_pass: bool = False

    # Cannot parse if only 1 number exists
    if length < 2:
        return

    while not full_pass:
        full_pass = True

        for i in range(length - 1):
            if (unsorted[i] > unsorted[i + 1]):
                unsorted[i], unsorted[i + 1] = swap(unsorted[i], unsorted[i + 1])
                full_pass = False