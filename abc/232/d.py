H, W = map(int, input().split())
C = []
for i in range(H):
    c = list(input())
    C.append(c)
#print(H, W, C)


def dfs():
    # W:行数、H:列数
    dist = [[-1]*W for _ in range(H)]  # 初期化
    dist[0][0] = 1  # 自分自身との距離は0

    s = [0, 0]
    st = [s]  # スタックを用意
    while st:
        #print('st=', st)
        v = st.pop()
        x, y = v[0], v[1]
        #print('v=', v, 'dist=', dist[x][y])
        # y軸方向に+1
        if x < H-1 and C[x + 1][y] == '.' and dist[x + 1][y] == -1:  # 外にはみ出てない&.である&未踏
            st.append([x + 1, y])
            dist[x + 1][y] = dist[x][y] + 1
        # x軸方向に+1
        if y < W-1 and C[x][y + 1] == '.' and dist[x][y + 1] == -1:
            st.append([x, y + 1])
            dist[x][y + 1] = dist[x][y] + 1
    return dist


dist0 = dfs()
tmp = [max(i) for i in dist0]
print(max(tmp))
