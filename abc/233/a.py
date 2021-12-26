import math
X, Y = map(int, input().split())
a = (Y - X) / 10
if a > 0:
    print(math.ceil((Y - X) / 10))
else:
    print(0)
