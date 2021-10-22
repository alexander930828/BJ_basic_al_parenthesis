import sys / 내가 쓴 오답

input = sys.stdin.readline
#
# n = int(input())
#
# for i in range(n):
#     string = str(input())
#     sen = []
#     for k in string:
#         sen.append(k)
#     if sen[0] == ')':
#         print("NO")
#     elif sen[-1] == '(':
#         print("NO")
#     else:
#         num1 = 0
#         num2 = 0
#         for j in sen:
#             if j == '(':
#                 num1 += 1
#             elif j == ')':
#                 num2 += 1
#         if num1 == num2:
#             print("YES")
#         else:
#             print("NO")

n = int(input())

for i in range(n):
    b = input()
    s = list(b)
    sum = 0
    for i in s:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0: # 첫번째로 ')'이 나올 일은 없어진다.
            print("NO")
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')