# n = str(input())
# for i in range(1, F) :
#     print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

n = int(input(), 16)

for i in range(1, 16) :
  print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')
  
'''
또는
print("%X*%X=%X"%(n,i,n*i))

'''
