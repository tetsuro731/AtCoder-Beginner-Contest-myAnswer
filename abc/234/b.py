import math

N = int(input())
X = []
Y = []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
#print(N, X, Y)

val = 0
for i in range(N):
    for j in range(i, N):
        val = max(val, (X[i]-X[j])**2 + (Y[i]-Y[j])**2)
print(math.sqrt(val))
