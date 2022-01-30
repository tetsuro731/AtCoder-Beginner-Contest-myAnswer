S = list(input())
a, b = map(int, input().split())
a = a - 1
b = b - 1
aa = S[a]
bb = S[b]
S[a] = bb
S[b] = aa
print(''.join(S))
