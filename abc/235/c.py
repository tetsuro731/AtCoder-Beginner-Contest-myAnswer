N, Q = map(int, input().split())
A = list(map(int, input().split()))
X = []
K = []
V = []
ans = {}
for i in range(Q):
    x, k = map(int, input().split())
    X.append(x)
    K.append(k)
    V.append(0)
dic_x = dict(zip(X, V))
#print('N, Q=', N, Q)
#print('A=', A)
#print('X,K=', X, K)
#print('dic=', dic_x)

for i, a in enumerate(A):
    if a in dic_x:
        dic_x[a] += 1
        ans[(a, dic_x[a])] = i + 1
#print('ans=', ans)

for i in range(len(K)):
    #print('x,k=', X[i], K[i])
    tup = (X[i], K[i])
    if tup not in ans:
        print(-1)
    else:
        print(ans[(X[i], K[i])])
