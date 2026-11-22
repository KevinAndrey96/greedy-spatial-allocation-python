"""
Bird Nest Allocation Algorithm

Problem Statement:
Write a function simulate_occupy(n), which demonstrates how birds occupy n nests,
assuming each new bird chooses the nest in the middle of the largest unoccupied run.
"""


def longest_false_run(nests):
    """
    Finds the start and end indices of the longest contiguous run of False values.
    Returns (start_index, length). If no False values exist, returns (-1, 0).
    """
    max_start = -1
    max_len = 0

    current_start = -1
    current_len = 0

    for i, occupied in enumerate(nests):
        if not occupied:
            if current_start == -1:
                current_start = i
                current_len = 1
            else:
                current_len += 1

            if current_len > max_len:
                max_len = current_len
                max_start = current_start
        else:
            current_start = -1
            current_len = 0

    return max_start, max_len


def occupy_step(nests):
    """
    Occupies the middle nest of the longest contiguous run of empty nests.
    Modifies the list in-place and returns the occupied index.
    """
    start, length = longest_false_run(nests)
    if start == -1 or length == 0:
        return -1

    # Choose middle index of the longest empty run
    mid_index = start + (length // 2)
    nests[mid_index] = True
    return mid_index


def format_nests(nests):
    """
    Formats the nests state as a readable string ('_' for empty, 'X' for occupied).
    """
    return " ".join("X" if occupied else "_" for occupied in nests)


def simulate_occupy(n):
    """
    Simulates the full sequence of birds occupying n nests until full.
    Prints each intermediate state.
    """
    nests = [False] * n
    states = [format_nests(nests)]

    for _ in range(n):
        occupy_step(nests)
        states.append(format_nests(nests))

    return states


if __name__ == '__main__':
    n = 10
    steps = simulate_occupy(n)
    for step in steps:
        print(step)
