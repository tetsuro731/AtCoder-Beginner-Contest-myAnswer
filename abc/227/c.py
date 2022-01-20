N = int(input())
count = 0
for a in range(1, N + 1):
    # a > N ** 1/3でもいいが、少数の処理がめんどい
    if a ** 3 > N:
        break
    tmp = N // a
    for b in range(a, N+1):
        c_max = tmp // b
        c_cnt = c_max - b + 1
        if c_cnt <= 0:
            break
        count += c_cnt
        #print('a, b, c_cnt=', a, b, c_cnt)
print(count)