import itertools

N, X = map(int, input().split())
A = []
for i in range(N):
    a = list(map(int, input().split()))
    A.append(a[1:])
#print(N, X)
#print(A)
ans = 0
for ii in itertools.product(*A):
    prod = 1
    for x in ii:
        prod *= x
        if prod > X:
            break
        #print('x, prod=', x, prod)
    if prod == X:
        ans += 1
print(ans)