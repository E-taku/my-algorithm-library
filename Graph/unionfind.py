# Union-Find 木
class Unionfind:
    # n 頂点の Union-Find 木を作成
    # (ここでは頂点番号が 1-indexed になるように実装しているが、0-indexed の場合は par,size のサイズは n でよい)
    def __init__(self,n):
        self.n = n
        self.par = [-1] * (n + 1) # 最初は親が無いので -1 で初期化
        self.size = [1] * (n + 1) # 最初はグループの頂点数が 1

    # 頂点　x の根を返す関数
    def root(self, x: int) -> int:
        # 1個先（親）がなくなる（つまり根に到着するまで）、１個先（親）に進み続ける
        while self.par[x] != -1:
            x = self.par[x]
        return x

    # 要素 u , v を結合する関数
    def unite(self, u: int,v: int) -> None:
        rootu = self.root(u)
        rootv = self.root(v)

        if rootu != rootv:
            # u , v が異なるグループのときのみ処理を行う
            if self.size[rootu] < self.size[rootv]:
                self.par[rootu] = rootv
                self.size[rootv] += self.size[rootu]
            else:
                self.par[rootv] = rootu
                self.size[rootu] += self.size[rootv]

    # 要素 u , v が同一のグループかどうかを返す関数
    def same(self, u: int, v: int) -> bool:
        return self.root(u) == self.root(v)



# 入力
N, Q = map(int, input().split())
queries = [ list(map(int, input().split())) for i in range(Q) ]

# クエリの処理
uf = Unionfind(N)
for tp, u, v in queries:
	if tp == 1:
		uf.unite(u, v)
	if tp == 2:
		if uf.same(u, v):
			print("Yes")
		else:
			print("No")