
# 定义棋盘大小
N = int(input())

# 所有可能的骑士移动
moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),
         (2, 1), (1, 2), (-1, 2), (-2, 1)]

def is_valid(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[y][x] == -1

def get_onward_moves_count(x, y, board):
    count = 0
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, board):
            count += 1
    return count

def next_move(x, y, board):
    min_deg = N + 1
    next_x, next_y = -1, -1
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, board):
            c = get_onward_moves_count(nx, ny, board)
            if c < min_deg:
                min_deg = c
                next_x, next_y = nx, ny
    if next_x == -1 and next_y == -1:
        return None
    return next_x, next_y

def knight_tour(start_x, start_y):
    board = [[-1 for _ in range(N)] for _ in range(N)]
    # 起点
    x, y = start_x, start_y
    board[y][x] = 0

    for move_num in range(1, N * N):
        next_pos = next_move(x, y, board)
        if not next_pos:
            return False
        x, y = next_pos
        board[y][x] = move_num
    return board

def print_board(board):
    for row in board:
        print(' '.join(f"{cell:2}" for cell in row))
    print()

# 执行并输出结果
start_x, start_y=map(int, input().split())
solution = knight_tour(start_x, start_y)
if solution:
    print('success')
else:
    print("fail")