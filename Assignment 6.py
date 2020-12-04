def board(rows, columns):
    for pos in range(1, rows + 1):
        print('0' * columns)
    return True


print(board(3, 4))
