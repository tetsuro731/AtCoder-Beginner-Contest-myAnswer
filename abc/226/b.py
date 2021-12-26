N = int(input())
li = [[int(j) for j in input().split()] for i in range(N)]
sliced = [tuple(i[1:]) for i in li[:]]
data_set = set(sliced)

print(len(data_set))