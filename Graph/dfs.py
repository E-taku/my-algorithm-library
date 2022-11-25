import sys
sys.setrecursionlimit(10 ** 9)
from collections import defaultdict

class dfs_timeStamp():
    """
    タイムスタンプ d[v]: v を最初に発見した発見時刻を記録します。
    タイムスタンプ f[v]: v の隣接リストを調べ終えた完了時刻を記録します。

    入力
    最初の行に G の頂点数 n が与えられる。続く n 行で各頂点 u の隣接リストが以下の形式で与えられる。
    u k v1 v2 ... vk

    出力
    各頂点について id、 d、 fを空白区切りで１行に出力。
    id は頂点の番号、d はその頂点の発見時刻、f はその頂点の完了時刻。頂点の番号順で出力。
    """

    def __init__(self):
        self.TIME = 0
        
    def input(self):
        self.N = int(input())
        self.G = defaultdict(list)
        self.d = [0] * (self.N+1) # 最初に発見した時刻
        self.f = [0] * (self.N+1) # 隣接リストを調べ終えた時刻

        for i in range(1,self.N+1):
            u,k,*v = map(int,input().split())

            if k != 0:
                self.G[u].extend(v)


    def dfs(self,pos: int, d: list, f: list):
        
        # 未訪問時の処理
        self.TIME += 1
        self.d[pos] = self.TIME  # 時刻の記録
        
        for next in self.G[pos]:
            if self.d[next] == 0: # 未探索の時（発見時刻が0のまま）
                self.dfs(next,self.d,self.f)

        # 帰る時の処理
        self.TIME += 1
        self.f[pos] = self.TIME # 繋がってる全ての点を探索し終えたらその点でやることは終わり
        
        return

    def output(self):
        for start in range(1, self.N+1):
           if self.d[start] == 0: # 未探索の点があれば
               self.dfs(start, self.d, self.f) # dfs開始

        for i in range(1, self.N+1):
           print(i, self.d[i], self.f[i])

time_stamp = dfs_timeStamp()
time_stamp.input()
time_stamp.output()





class Single_path():
    """
    頂点数 N、辺数 M の連結なグラフが与えられる。 このグラフについて、頂点 1 から頂点 N までの単純パスを一つ出力。

    """
    def __init__(self):
        self.path = []

    def input(self):
        self.N,self.M = map(int,input().split())

        self.G = defaultdict(list)

        for i in range(self.M):
            a,b = map(int,input().split())
            self.G[a].append(b)
            self.G[b].append(a)



    def simple_path(self):
        visited = [False] * (self.N+1)
        def dfs(self,i: int):
            self.path.append(i)
            if i == self.N:
                print(*self.path)
                exit()
                return self.path
            visited[i] = True
            for next in self.G[i]:
                if visited[next] == False:
                    dfs(self,next)
            self.path.pop()
        dfs(self,1)

sp = Single_path()
sp.input()
sp.simple_path()





