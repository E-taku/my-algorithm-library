# L: リスト
# 何回swapしたか返す
def bubblesort(L:list, N:int):
    cnt = 0 # 何回swapするか
    for i in range(N-1):
        for j in range(N-i-1):
            if L[j] > L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]
                cnt += 1
    return cnt