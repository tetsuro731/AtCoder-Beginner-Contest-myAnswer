# 例外の場合分けが必要。A問題にしては難しい
N, K, A = map(int, input().split())
mod = (A + K - 1) % N
ans = mod
if mod == 0:
    ans = N
print(ans)
