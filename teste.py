board = list()
rowList = list()

for row in range(0, 10):
    for col in range(0, 10):
        rowList.append(0)
    board.append(rowList[:])
    rowList.clear()

board[0][9] = 1
board[9][0] = 1
board[8][0] = 1


#Moving to right
for row in range(len(board)):
    for col in range(len(board[row])):
        if col < len(board) - 1 and board[row][col] == 1:
            board[row][col + 1] = 1
            board[row][col] = 0
            break

#Moving to left
for row in range(len(board)):
    for col in range(len(board[row])):
        if col > 0 and board[row][col] == 1:
            board[row][col - 1] = 1
            board[row][col] = 0
            break

#Moving to down
for row in range(len(board) - 2, -1, -1):
    for col in range(len(board[row])):
        if board[row][col] == 1:
            if board[row + 1][col] != 1:
                board[row + 1][col] = 1
                board[row][col] = 0

for row in range(len(board)):
    print(board[row])
