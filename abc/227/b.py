N = int(input())
S_list = [int(i) for i in input().split()]
#print(N,S_list)

false_sum = 0
for s in S_list:
    false_flag = 1
    for a in range(150):
        for b in range(150):
            a = a+1
            b = b+1
            if 4*a*b + 3*(a+b) == s:
                false_flag = 0
    false_sum += false_flag
print(false_sum)
