board = []
x = 1
y = 1

# 2차배열 input
for i in range(10):
    temp = list(map(int,input().split()))
    board.append(temp)
    
while True:
    if board[x][y] == 2: #먹이를 발견했을때
        board[x][y] = 9
        break
    elif board[x+1][y] == 1 and board[x][y+1] == 1: #가로막혔을때
        board[x][y] = 9
        break
    board[x][y] = 9
    if board[x][y+1] == 1: # 오른쪽이 벽이면 아래로 1칸
        x += 1
    elif board[x+1][y] == 1: # 아래쪽이 벽이면 오른쪽으로 1칸
        y += 1
    else: y += 1 # 주변에 벽이 없으면 오른쪽으로 1칸

for a in board:
    for b in a:
        print(b,end=' ')
    print()