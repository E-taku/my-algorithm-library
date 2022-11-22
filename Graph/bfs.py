from collections import defaultdict
from collections import deque

# まず隣接リストを求める
N,M = map(int,input().split())
G = defaultdict(list)
for i in range(M):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)



class Bfs:

    # 重みなし無効グラフに対する最短経路問題
    def shortest_path_length(N: int, G: dict) -> list:
        """_summary_
        頂点 1 から頂点 k まで、辺を何本かたどって移動することを考えるとき、たどるべき辺の本数の最小値を出力。ただし、移動不可能な場合は −1 を出力。

        Args:
            N (int): 頂点数
            M (int): 辺数
        """
        G = defaultdict(list)
        dist = [-1] * (N+1)
        dist[1] = 0
        Q = deque()
        Q.append(1)

        # 幅優先探索
        while Q:
            pos = Q.popleft()
            for next in G[pos]:
                if dist[next] == -1:
                    dist[next] = dist[pos] + 1
                    Q.append(next)
        return dist

    # 迷路
    # スタート地点からゴール地点まで最短何手でいけるか
    def maze_shortest_move(maze: list, sy: int,sx: int,gy: int,gx: int) -> int:
        """_summary_
        https://atcoder.jp/contests/tessoku-book/tasks/abc007_3
        Args:
            maze (list): _description_
            sy (int): スタート地点のy座標
            sx (int): スタート地点のx座標
            gy (int): ゴール地点のy座標
            gx (int): ゴール地点のx座標

        Returns:
            int: ゴールまでの最短手
        """
        # (y,x) ←↓↑→
        directions = [(0,-1),(1,0),(-1,0),(0,1)]
        maze[sy-1][sx-1] = 0
        Q = deque()
        Q.append((sy-1,sx-1))

        # 幅優先探索
        while Q:
            pos = Q.popleft()
            for y,x in directions:
                y = pos[0] + y
                x = pos[1] + x
                to = (y,x)
                if maze[y][x] == '#':
                    continue
                if maze[y][x] == '.':
                    maze[y][x] = maze[pos[0]][pos[1]] + 1
                    Q.append(to)

        return maze[gy-1][gx-1]



