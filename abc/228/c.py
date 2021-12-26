N, K = map(int, input().split())
P = []
for j in range(N):
    s = sum([int(i) for i in input().split()])
    P.append(s)
#print(N, K, P)
sort_score = sorted(P)[-K]
#print(sort_score)

for i in range(N):
    #print(P[i] - sort_score)
    if P[i] - sort_score < -300:  # 300点以上差があると逆転不可能
        print('No')
    else:
        print('Yes')