import io
import sys
import time
_INPUT = """\
4 2
1 3
2 3
"""
StartTime = time.time()
sys.stdin = io.StringIO(_INPUT)
#____________________________________________
N, M = map(int, input().split())
A = []
B = []
D = dict()

# 無向グラフ, list連結
G = [[] for i in range(N)]
# dfsで閉路があるかをチェックする
visited = [0] * N
def dfs(s):
    dist = [-1] * N  # 初期化
    dist[s] = 0  # 自分自身との距離は0
    st = [s]  # スタックを用意
    #visited[s] = 1  # 訪問済み
    cycle_flag = False
    while st:
        v = st.pop()
        print('v=', v)
        for nv in G[v]:
            print('nv=', nv)
            if nv == v:  # 元の道を戻るような回路は閉路ではないので除く
                continue
            if dist[nv] == -1:
                st.append(nv)
                dist[nv] = dist[v] + 1
            else:
                cycle_flag = True
    return cycle_flag


for i in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    A.append(a)
    B.append(b)
    # Gはdfs用
    G[a].append(b)
    G[b].append(a)
    if a in D and b in D:
        continue
    if a not in D:
        D[a] = 1
    else:
        D[a] += 1
    if b not in D:
        D[b] = 1
    else:
        D[b] += 1
    #print('D=', D)
    # 両端が3個以上のものはありえない
    if D[a] > 2 or D[b] > 2:
        print('No')
        exit(0)


print('G=', G)
for a in A:
    # 0から最も遠い点を求める
    print('a=', a)
    cycle = dfs(a)
    print(cycle)



print('Yes')
#____________________________________________
print ("[Sec]"+str(time.time() - StartTime))
