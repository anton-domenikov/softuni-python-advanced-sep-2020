def best_list_pureness(*args):
    from collections import deque
    import sys
    best_pureness = -sys.maxsize
    best_rotation = 0
    numbers = deque(args[0])
    k = args[1]

    for rotation in range(k+1):
        curr_pureness = 0
        for i, num in enumerate(numbers):
            curr_pureness += i * num
            # print(curr_pureness)
        if curr_pureness > best_pureness:
            best_pureness = curr_pureness
            best_rotation = rotation
        print(f'for rotation {rotation} pureness is {curr_pureness}')
        numbers.rotate(1)
        print(numbers)

    return f'Best pureness {best_pureness} after {best_rotation} rotations'

# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
# test = ([1, 2, 3, 4, 5], 10)
# result = best_list_pureness(*test)
# print(result)
