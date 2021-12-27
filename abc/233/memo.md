## 223
### A
- 割り算して切り上げるだけ
### B
- stringの一部分を切り取って反転するだけ
### C
- 愚直な方法で解ける
- for文がN回ネストするのでitertools.product()を使った
### D
- 累計和を予め計算しておく
- それでも愚直にやるとO(N^2)なのでLTE
- lからrまでの部分和は累積和を用いると
  - sum_list(r) - sum_list(l) = K
- rが決まったときに sum_list(l) = sum_list(r) - K を満たせば良い
- これを満たすかどうかをdict型で保存しておけば、一回のループで計算可能
- Pythonの場合はdict型をラップしたcollections.Counter() を使うと便利
