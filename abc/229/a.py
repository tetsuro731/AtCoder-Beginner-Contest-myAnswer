S1 = input()
S2 = input()
#print(S1, S2)
if S1 == '##' or S2 == '##':
    print('Yes')
elif S1 == '#.' and S2 == '#.':
    print('Yes')
elif S1 == '.#' and S2 == '.#':
    print('Yes')
else:
    print('No')
