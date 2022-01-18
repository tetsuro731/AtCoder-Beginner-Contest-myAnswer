from collections import deque

a, N = map(int, input().split())
#print('a,N=', a, N)
# Nより大きいM=10**nを計算する
# Mは距離を格納するindexとして使用する
M = 1
while M <= N:
    M *= 10

dist = [-1] * M  # -1で初期化しておく
dist[1] = 0  # 最初の点は距離0
deq = deque([1])  # queを用意
while deq:
    #print('deq=',deq)
    #print('dist=',dist)
    v = deq.popleft()
    dist0 = dist[v]
    # 2パターン
    x1 = v * a
    #print('x1=', x1)
    if x1 < M and dist[x1] == -1:
        deq.append(x1)
        dist[x1] = dist0 + 1
        #print('dist=', dist[x1])
    x2 = int(str(v)[-1] + str(v)[:-1])
    #print('x2=', x2)
    if x2 < M and dist[x2] == -1 and v >= 10 and v % 10 != 0:  # 問題文の要請から
        deq.append(x2)
        dist[x2] = dist0 + 1
        #print('dist=', dist[x2])
print(dist[N])
