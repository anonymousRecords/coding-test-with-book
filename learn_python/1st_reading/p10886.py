N = int(input())
cute = 0
not_cute = 0
for i in range(1, N+1):
    choice = int(input())
    if choice == 1:
        cute += 1
    elif choice == 0:
        not_cute += 1
    else:
        continue

if cute > not_cute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")