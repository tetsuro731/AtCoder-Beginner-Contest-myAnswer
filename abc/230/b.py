S = input()
#print(len(S))
if len(S) == 1 and (S[0] == 'x' or S[0] == 'o'):
    print('Yes')
    exit(0)
if len(S) == 2 and (S[:2] == 'ox' or S[:2] == 'xo' or S[:2] == 'xx'):
    print('Yes')
    exit(0)

first = S[:3]
if first != 'xxo' and first != 'xox' and first != 'oxx':
    print('No')
    exit(0)

for i, s in enumerate(S):
    mod = i % 3
    if s != first[mod]:
        print('No')
        exit(0)
print('Yes')