N, M = map(int, input().split())
S = list(input().split())
T = list(input().split())
Tdict = {i:True for i in T}
for s in S:
    if s in Tdict:
        print('Yes')
    else:
        print('No')