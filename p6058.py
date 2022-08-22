# a, b = input().split()
# answer = not (bool(int(a)) or bool(int(b)))
# if answer == False :
#     print(True)
# else : 
#     print(False)
# print(bool(0))
# print(bool(1))
# answer = bool(0) and bool(1)
# print(answer)

a, b = input().split()
if bool(int(a)) == bool(int(b)) == False :
    print(True)
else :
    print(False)