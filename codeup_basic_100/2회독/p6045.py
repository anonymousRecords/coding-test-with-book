# a, b, c = map(int, input().split())
# print(a+b+c, round((a+b+c)/3,2))

# a,b,c = map(int,input().split())
# average = '.2f' %round((a+b+c)/3)
# print(a+b+c, average) 내 코드

a, b, c = map(int, input().split())
avg = (a+b+c)/3

print(a+b+c)
print("%0.2f" % avg)
