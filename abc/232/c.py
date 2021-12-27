import itertools
N, M = map(int, input().split())
#print(N, M)

AB = [[0] * N for i in range(N)]
CD = [[0] * N for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    AB[a][b] = 1
    AB[b][a] = 1
for i in range(M):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    CD[c][d] = 1
    CD[d][c] = 1
#print('AB=', AB)
#print('CD=', AB)

ans = False
for p in itertools.permutations(range(N)):
    flag = True
    #print('p=',p)
    for i in range(N):
        for j in range(N):
            if AB[i][j] != CD[p[i]][p[j]]:
                flag = False
    if flag:
        ans = True
if ans:
    print('Yes')
else:
    print('No')