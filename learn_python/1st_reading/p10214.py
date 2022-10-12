T = int(input())
for i in range(1, T+1):
    sum_Y = 0
    sum_K = 0
    for i in range(1, 10):
        Y, K = map(int, input().split())
        sum_Y += Y
        sum_K += K

    if sum_Y > sum_K:
        print("Yonsei")
    elif sum_Y < sum_K:
        print("Korea")
    else:
        print("Draw")