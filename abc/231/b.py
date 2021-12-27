N = int(input())
S = dict()
for i in range(N):
    key = input()
    #print(i, key)
    if key in S:
        S[key] += 1
    else:
        S[key] = 1
#print(N, S)
print(max(S, key=S.get))
