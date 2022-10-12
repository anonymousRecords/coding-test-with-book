n = int(input())
j_score = 100
c_score = 100
for i in range(1, n+1):
    j, c = map(int, input().split())
    if j > c:
        c_score -= j
    elif j < c:
        j_score -= c
    else:
        continue
print(j_score)
print(c_score)
