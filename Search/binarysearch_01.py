class BinarySearch_01:
    def __init__(self, x: int, A: list) -> None:
        self.x = x # 探したい値
        self.A = sorted(A) # 配列
        self.N = len(A)
        self.idx = self.search()

    def search(self) -> None:
        L = 0
        R = self.N - 1

        while L <= R:
            M = (L + R) // 2
            if self.x < self.A[M]:
                R = M - 1
            if self.x == self.A[M]:
                return M + 1
            if self.x > self.A[M]:
                L = M + 1
        return -1
