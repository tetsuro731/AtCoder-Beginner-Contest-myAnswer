N = int(input())
H = list(map(int, input().split()))
val = 0
for i in H:
    if i <= val:
        break
    val = i
print(val)
