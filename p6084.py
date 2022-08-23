# h, b, c = input().split()
# h = float(h)
# b = int(b)
# c = int(c)
# print((h*1000) * (b*2*c)//8//1024//1024)

h,b,c,s = map(int, input().split())
print(round(h*b*c*s/8/1024/1024,1),'MB')