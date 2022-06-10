def get_edit_cost(original: str, goal: str) -> int:
    '''
    Calculate cost to edit first argument into second argument using recursion
    '''
    # Write your answer here.
    if len(original) == 0:
        return len(goal)
    if len(goal) == 0:
        return len(original)

    val1 = 1 + get_edit_cost(original, goal[1:])
    val2 = 1 + get_edit_cost(original[1:], goal)

    if original[0] == goal[0]:
        val3 = get_edit_cost(original[1:], goal[1:])
    else:
        val3 = 1 + get_edit_cost(original[1:], goal[1:])
    return min(val1, val2, val3)


print(get_edit_cost("kitten", "sitting"))     # 3
print(get_edit_cost("info1110", "1110"))      # 4
print(get_edit_cost("pass", "sparse"))        # 3
