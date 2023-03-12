"""
めぐる式二分探索の実装
https://qiita.com/drken/items/97e37dd6143e33a64c8c

binary_search_left
- 挿入できるリストの添字を返します。同じ値がある場合は、その値の最も左側の添字になります。

binary_search_right
- 挿入できるリストの添字を返します。同じ値がある場合は、その値の最も右側の添字になります。

li = [2, 5, 8, 13, 13, 18, 25, 30]

ind = binary_search_left(li, 10)
print(ind) # 3

ind = binary_search_left(li, 13)
print(ind) # 3


ind = binary_search_right(li, 10)
print(ind) # 3

ind = binary_search_right(li, 13)
print(ind) # 5
"""


def is_ok_left(li: list, key: int, mid: int) -> bool:
    return key <= li[mid]

def binary_search_left(li: list, key: int) -> int:
    ng = -1
    ok = len(li) # N
    while abs(ok - ng) > 1:
        mid = (ng + ok) // 2
        if is_ok_left(li, key, mid):
            ok = mid
        else:
            ng = mid
    return ok

def is_ok_right(li: list, key: int, mid: int) -> bool:
    return key < li[mid]

def binary_search_right(li: list, key: int) -> int:
    ng = -1
    ok = len(li) # N
    while abs(ok - ng) > 1:
        mid = (ng + ok) // 2
        if is_ok_right(li, key, mid):
            ok = mid
        else:
            ng = mid
    return ok
