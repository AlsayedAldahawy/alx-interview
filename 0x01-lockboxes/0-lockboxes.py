#!/usr/bin/python3

"""
    Determines whether all boxes in a list of boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines whether all boxes in a list of boxes can be unlocked.

    Args:
        boxes (list of lists): A list of boxes, where each box is represented
        by a list of keys (integers).

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.

    Example:
        >>> boxes = [[1], [2, 3], [0], ['unlocked']]
        >>> canUnlockAll(boxes)
        True
    """
    boxesLen = len(boxes)
    stucked = True
    allUnlocked = True
    allkeys = boxes[0][:]

    # Check if all boxes are already unlocked
    for box in boxes[1:]:
        if box != 'unlocked':
            allUnlocked = False
            break
    if allUnlocked:
        return allUnlocked

    # Check if any box is stuck (cannot be unlocked)
    for i in range(1, boxesLen):
        if boxes[i] == "unlocked":
            continue
        if i in boxes[0]:
            stucked = False
    if stucked:
        return False

    # Collect keys from unlocked boxes
    for key in boxes[0]:
        try:
            if boxes[key] != "unlocked":
                allkeys += boxes[key]
                boxes[key] = "unlocked"
        except (KeyError, IndexError):
            continue

    # Recursively check remaining boxes
    return canUnlockAll([list(set(allkeys))] + boxes[1:])
