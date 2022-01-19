#  input.............................
N = int(input())
N, Q = map(int, input().split())
A = list(map(int, input().split()))
print('N, Q=', N, Q)

X = []
K = []
for i in range(N):
    x, k = map(int, input().split())
    X.append(x)
    K.append(k)

for i in range(Q):
    a = int(input().split()))
    A.append()

# for..................
for i, v in enumerate(A):
    print(i,v)
# 行列、二次元配列
AB = [[0] * N for i in range(N)]
CD = [[0] * N for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
a, b = a - 1, b - 1
AB[a][b] = 1
AB[b][a] = 1

# dfs.......................
N = int(input())
# 無向グラフ, list連結
G = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)

# 深さ優先探索
# ある点sから各点までの距離をdistに格納
def dfs(s):
    dist = [-1] * N  # 初期化
    dist[s] = 0  # 自分自身との距離は0
    st = [s]  # スタックを用意
    while st:
        v = st.pop()
        for nv in G[v]:
            if dist[nv] == -1:
                st.append(nv)
                dist[nv] = dist[v] + 1
    return dist


# 0から最も遠い点を求める
dist0 = dfs(0)
index = dist0.index(max(dist0))
# その点からさらに最も遠い点を求め、長さを直径とする
r_dist = dfs(index)
# 直径に1を加えたものが答えとなる
print(max(r_dist) + 1)

# bfs..................
from collections import deque
def bfs(s):
    dist = [-1] * N  # 初期化
    dist[s] = 0  # 自分自身との距離は0
    deq = deque([s]) # queを用意
    while deq:
        v = deq.popleft()
        for nv in G[v]:
            if dist[nv] == -1:
                deq.append(nv)
                dist[nv] = dist[v] + 1
    return dist.....

