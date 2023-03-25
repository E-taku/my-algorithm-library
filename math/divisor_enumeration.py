# 約数列挙 O(√N)
def div(M):
    res=set()
    i=1
    while(i*i<=M):
        if M%i==0:
            res.add(i)
            res.add(M//i)
        i+=1
    return res
