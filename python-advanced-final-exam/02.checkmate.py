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
