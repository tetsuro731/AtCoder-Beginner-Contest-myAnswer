S = input()
T = input()
dif = ord(T[0]) - ord(S[0])
if dif < 0:
    dif += 26
#  print(dif)
#  print('i=', i)
str = ''
for s in S:
    stmp = ord(s) + dif
    if stmp >= 123:
        stmp -= 26
    stmp = chr(stmp)
    str += stmp
    s_last = stmp
if str == T:
    print('Yes')
    exit(0)
print('No')
