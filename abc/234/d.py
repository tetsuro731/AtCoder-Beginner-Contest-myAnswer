import heapq as hq
N, K = map(int, input().split())
P = list(map(int, input().split()))
#print(N, K, P)

que = []
# 最初のK個の要素をheapqに格納
for p in P[:K]:
    hq.heappush(que, p)

# 最初のK個の中で最小の要素が最初の答え
print(que[0])
for p in P[K:]:
    hq.heappush(que, p)  # 要素を1つheapに加える
    hq.heappop(que)  # 常にK番目に大きい値が知りたいので、一番小さい要素をpop
    print(que[0])  # この時点での最小値が答え


