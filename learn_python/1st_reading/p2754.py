# score = float(input())
# A0 = 4.0
# B0 = 3.0
# C0 = 2.0
# D0 = 1.0
# if score > 3.7:
#     if score >= 4.3:
#         print('A+')
#     elif score >= 4.0:
#         print('A0')
#     else:
#         print('A-')
# elif score > 2.7:
#     if score >= 3.3:
#             print('B+')
#     elif score >= 3.0:
#         print('B0')
#     else:
#         print('B-')
# elif score > 1.7:
#     if score >= 2.3:
#             print('C+')
#     elif score >= 2.0:
#         print('C0')
#     else:
#         print('C-')
# elif score > 0.7:
#     if score >= 1.3:
#             print('D+')
#     elif score >= 1.0:
#         print('D0')
#     else:
#         print('D-')
# else:
score = str(input())
if score == 'A+':
    print(4.3)
elif score == 'A0':
    print(4.0)
elif score == 'A-':
    print(3.7)
elif score == 'B+':
    print(3.3)
elif score == 'B0':
    print(3.0)
elif score == 'B-':
    print(2.7)
elif score == 'C+':
    print(2.3)
elif score == 'C0':
    print(2.0)
elif score == 'C-':
    print(1.7)
elif score == 'D+':
    print(1.3)
elif score == 'D0':
    print(1.0)
elif score == 'D-':
    print(0.7)
elif score == 'F':
    print(0.0)
else:
    print()