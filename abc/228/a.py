S, T, X = map(int, input().split())
#print(S, T, X)
if S < T:
    if S <= X and X < T:
        print('Yes')
    else:
        print('No')
else:
    T = T + 24
    X2 = X + 24
    if (S <= X and X < T) or(S <= X2 and X2 < T):
        print('Yes')
    else:
        print('No')
