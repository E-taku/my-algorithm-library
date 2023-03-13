"""
nを素因数分解

n = p1^e1 * pc^e2 * ... * pm^em
p1, p2, ..., pm : 素因数
e1, e2, ..., em : 指数

return : 2以上の整数n => [[素因数, 指数], ...]の2次元リスト
"""

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
