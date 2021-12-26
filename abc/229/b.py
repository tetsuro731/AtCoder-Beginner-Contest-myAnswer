A, B = input().split()
A = A[::-1]
B = B[::-1]
#print(A, B)
#print(len(A), len(B))

length = len(A)
if len(A) >= len(B):
    length = len(B)

flag = 0
for i in range(length):
    #print('i=', i)
    #print(A[i], B[i])
    sum = int(A[i]) + int(B[i])
    if sum > 9:
        flag = 1
if flag == 1:
    print('Hard')
else:
    print('Easy')