N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())
X = Q - P + 1
Y = S - R + 1
l = [['.' for i in range(Y)] for j in range(X)]
#print('N, A, B=', N, A, B)
#print('P, Q, R, S=', P, Q, R, S)
#print(l)

#low1, high1 = max(1-A, 1-B), min(N-A, N-B) #本来の条件
#low2, high2 = max(1-A, B-N), min(N-A, B-1)
low1, high1 = max(P-A, R-B), min(Q-A, S-B)
low2, high2 = max(P-A, B-S), min(Q-A, B-R)
#print('low1, high1=', low1, high1)
#print('low2, high2=', low2, high2)
for k in range(low1, high1 + 1):
    #print('1st:',k, A+k, B+k)
    l[A+k-1-(P-1)][B+k-1-(R-1)] = '#'
for k in range(low2, high2 + 1):
    #print('2nd:', k,  A+k, B-k)
    l[A+k-1-(P-1)][B-k-1-(R-1)] = '#'

for x in l:
    print(*x, sep='')