N = int(input())
A = list(map(int, input().split()))
l = [0 for i in range(N)]
for i in range(4 * N - 1):
    l[A[i]-1] += 1
for i in range(N):
    if l[i] == 3:
        print(i + 1)

