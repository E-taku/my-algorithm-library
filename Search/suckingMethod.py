class SuckingMethod:
    def choose_pairs_two_integers(self,N: int,K: int, A: list):
        """
        小さい順に A1,A2,⋯,AN です。
        異なる 2 つの整数のペアを選ぶ方法は全部で N(N−1)/2 通りあるが、
        その中で差が K 以下であるような選び方は何通りあるか。
        """
        R = [None] * (N)
        # 尺取法
        for i in range(N-1):
            # スタート地点を決める
            if i == 0:
                R[0] = 0
            else:
                R[i] = R[i-1]
            # 増やせるとことまで増やす
            while (R[i] < N - 1) and (A[R[i] + 1] - A[i]) <= K:
                R[i] += 1
        ans = 0
        for i in range(N-1):
            ans += (R[i] - i)
        return ans


