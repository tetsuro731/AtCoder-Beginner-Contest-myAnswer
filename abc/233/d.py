import collections
N, K = map(int, input().split())
A = list(map(int, input().split()))

#print(K, A)
# 部分和を計算しておく
# 後の計算のために最初を0埋めしておく
sum_list = [0]
tmp_sum = 0
ccl = collections.Counter([0])
ans = 0
for l in range(N):
    tmp_sum += A[l]
    sum_list.append(tmp_sum)  # 累積和の計算
    ans += ccl[sum_list[l + 1] - K]  # 条件を満たす部分和がいくつ存在するか
    ccl[sum_list[l + 1]] += 1  # 部分和の数を記録
print(ans)
