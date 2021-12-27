import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
X = []
for i in range(Q):
    X.append(int(input()))

#print('N, Q, A=', N, Q, A)
#print('X=', X)
for x in X:
    num = bisect.bisect_left(A, x)
    #print('x=', x, 'num=', num)
    print(len(A) - num)
