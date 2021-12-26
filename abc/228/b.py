import sys
sys.setrecursionlimit(1000000)
#print(sys.getrecursionlimit())

ans_set = set()

def add_set(a):
    ans_set.add(a)
    next_a = A[a-1]
    #print('a, nex_a=', a, next_a)
    if next_a in ans_set:
        print(len(ans_set))
    else:
        add_set(next_a)

N, X = map(int, input().split())
A = [i for i in map(int, input().split())]
#print(N, X, A)

add_set(X)