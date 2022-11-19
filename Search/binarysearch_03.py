class Binary_search():
    def __init__(self, x: int, A: list) -> None:
        self.x = x # 探したい値
        self.A = A # ソートした配列
        self.N = len(A)

    def search(self,A: list, x: int):
        L = 0
        R = self.N - 1

        while L <= R:
            M = (L + R) // 2
            if x < A[M]:
                R = M - 1
            if x == A[M]:
                return True
            if x > A[M]:
               L = M + 1
        return False


