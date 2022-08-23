# n, m = input().split()
# n = int(n)
# m = int(m)
# for i in range(1, n+1) :
#     for j in range(1, m+1) :
#         print(i, j)

# r, g, b= input().split()
# r = int(r)
# g = int(g)
# b = int(b)
# for i in range(1, r+1) :
#     for j in range(1, g+1) :
#         for k in range(1, b+1) :
#             print(r, g, b)

r,g,b=map(int, input().split())

for i in range(r):

    for j in range(g):

        for k in range(b):

            print(i,j,k)

print(r*g*b)