L, R = map(int, input().split())
S = input()
S1 = S[:L-1]
S2 = S[L-1:R]
S2 = S2[::-1]
S3 = S[R:]
print(S1 + S2 + S3)
