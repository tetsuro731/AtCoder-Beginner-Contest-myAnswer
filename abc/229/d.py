S = input()
K = int(input())
#print(S, K)

sum = 0
sum_l = [0]  # 累積和
for s in S:
    if s == '.':
        sum += 1
    sum_l.append(sum)
#print(sum_l)

ans = 0
r = 0
n = len(S)
for l in range(n):
    #print('l=', l)
    while r < n and sum_l[r+1] - sum_l[l] <= K:
        r = r + 1
        #print('r=', r)
        #print('sumr, suml, sumr-l=', sum_l[r], sum_l[l], sum_l[r] - sum_l[l])
    ans = max(ans, r - l)
    #print('ans=', ans)
print(ans)
