# https://note.nkmk.me/python-union-find/

from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        """
        n個の要素を 0 ~ n - 1 の番号で管理する
        各要素の親要素の番号を格納するリスト
        要素が根（ルート）の場合は-(そのグループの要素数)を格納する
        """
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        """
        要素xが属するグループの根を返す
        """
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """
        要素xが属するグループと要素yが属するグループとを併合する
        """
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        """
        要素xが属するグループのサイズ（要素数）を返す
        """
        return -self.parents[self.find(x)]

    def same(self, x, y) -> bool:
        """
        要素x, yが同じグループに属するかどうかを返す
        """
        return self.find(x) == self.find(y)

    def members(self, x):
        """
        要素xが属するグループに属する要素をリストで返す
        """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """
        すべての根の要素をリストで返す
        """
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """
        グループの数を返す
        """
        return len(self.roots())

    def all_group_members(self):
        """
        {ルート要素: [そのグループに含まれる要素のリスト], ...}のdefaultdictを返す
        """
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        """
        print()での表示用
        ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す
        f文字列を利用している
        """
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


# 文字列やタプルなどを要素とする場合
# 上の例のクラスでは要素の個数nを指定し、n個の要素を0 ~ n - 1の番号で管理する。find()やunion()などの引数にはその番号を指定する。
# 例えば人の名前や都市の名前など何らかの文字列を元にUnion Findデータ構造を構成して処理したい場合は、文字列と番号のペアの辞書を用意すると便利。
# {文字列: 番号, ... }と{番号: 文字列, ...}の辞書をそれぞれ用意する。ここでは辞書内包表記を使う。

# l = ['A', 'B', 'C', 'D', 'E']

# d = {x: i for i, x in enumerate(l)}
# print(d)
# # {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}

# d_inv = {i: x for i, x in enumerate(l)}
# print(d_inv)
# # {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}


class UnionFindLabel(UnionFind):
    def __init__(self, labels):
        assert len(labels) == len(set(labels))

        self.n = len(labels)
        self.parents = [-1] * self.n
        self.d = {x: i for i, x in enumerate(labels)}
        self.d_inv = {i: x for i, x in enumerate(labels)}

    def find_label(self, x):
        return self.d_inv[super().find(self.d[x])]

    def union(self, x, y):
        super().union(self.d[x], self.d[y])

    def size(self, x):
        return super().size(self.d[x])

    def same(self, x, y):
        return super().same(self.d[x], self.d[y])

    def members(self, x):
        root = self.find(self.d[x])
        return [self.d_inv[i] for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [self.d_inv[i] for i, x in enumerate(self.parents) if x < 0]

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.d_inv[self.find(member)]].append(self.d_inv[member])
        return group_members
