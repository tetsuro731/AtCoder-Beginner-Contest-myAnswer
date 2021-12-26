N, W = map(int, input().split())
AB = []

for i in range(N):
    a, b = map(int, input().split())
    AB.append([a, b])

AB.sort(reverse=True)

weight = 0
oishi = 0
for i in range(N):
    tmp_w = AB[i][1]
    tmp_o = AB[i][0]
    if W - weight > tmp_w:
        oishi += tmp_w * tmp_o
        weight += tmp_w
    elif W - weight > 0:
        oishi += (W - weight) * tmp_o
        weight += (W - weight)
    else:
        break
print(oishi)
