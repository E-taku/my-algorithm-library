def rle(s):
    res = []
    cnt = 1
    for i in range(len(s)):
        if i == len(s) - 1:
            res.append((s[i], cnt))
        else:
            if s[i] == s[i+1]:
                cnt += 1
            else:
                res.append((s[i], cnt))
                cnt = 1
    return res
