import itertools

N = int(input())
li = [[int(j) for j in input().split()] for i in range(N)]
T = [i[0] for i in li[:]]
A = [i[2:] for i in li[:]]

T_sum = 0
N_list = [N]  # targetのnのlist
A_master_set = set()
# print(T, A)
for i in range(1000000):
    # print('i=', i)
    T_list = [T[j - 1] for j in N_list] # ターゲットの時間のlist

    T_sum += sum(T_list) # 時間の和
    A_list = [A[j - 1] for j in N_list]
    A_list = list(itertools.chain.from_iterable(A_list)) # 2重listを1重にする
    # A_listから習得済みを除く
    A_list = list(set(A_list) - A_master_set)
    for k in A_list:
        A_master_set.add(k)  # 習得済みのsetに追加
    # print(T_list, T_sum, A_list)
    N_list = A_list  # N_listを更新
    if len(A_list) == 0:  # 次のターゲットがなくなれば終了
        break
print(T_sum)
