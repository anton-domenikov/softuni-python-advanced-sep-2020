# 1 ==========================================================================
from collections import deque

jobs = deque(map(int, input().split(', ')))
index = int(input())

cycles = 0
target_num = jobs[index]

while True:
    min_num = min(jobs)
    min_num_index = jobs.index(min_num)

    if min_num_index == index:
        cycles += min_num
        break

    if min_num_index < index:
        cycles += min_num
        del jobs[min_num_index]
        index -= 1

    if min_num_index > index:
        cycles += min_num
        del jobs[min_num_index]

print(cycles)


# 2 ==========================================================================
def is_valid(i, j):
    return 0 <= i < 8 and 0 <= j < 8


chess_board = [list(input().split()) for row in range(8)]
is_the_king_safe = 'The king is safe!'

queens = [[row, col] for row in range(8) for col in range(8) if chess_board[row][col] == 'Q']
queens_that_kill_king = []

for queen in queens:
    possible_moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for move in possible_moves:
        i = move[0] + queen[0]
        j = move[1] + queen[1]
        while is_valid(i, j):
            if chess_board[i][j] == 'K':
                is_the_king_safe = False
                queens_that_kill_king.append(queen)
                break
            elif chess_board[i][j] == 'Q':
                break
            else:
                i += move[0]
                j += move[1]

if is_the_king_safe:
    print(is_the_king_safe)
else:
    for q in queens_that_kill_king:
        print(q)


# 3 ==========================================================================
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
