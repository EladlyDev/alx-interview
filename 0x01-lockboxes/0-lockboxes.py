#!/usr/bin/python3
""" Lockboxes module """


def canUnlockAll(boxes):
    """
    Check if all lockboxes can be unlocked.

    Args:
        boxes (list): A list of lists representing the lockboxes.
        Each inner list contains the keys to other lockboxes.

    Returns:
        bool: True if all lockboxes can be unlocked, False otherwise.
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
