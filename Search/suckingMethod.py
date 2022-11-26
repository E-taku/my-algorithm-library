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

    def cumulativeSum_choose_pairs_two_integers(self,N: int,K: int, A: list):
        """
        i 番目の品物は Ai円です。連続する番号の品物を買う方法
        その中で差が K 以下であるような選び方は何通りあるか。
        累積和と尺取法を組み合わせる
        """
        S = [0] * (N+1)

        # 累積和
        for i in range(1,N+1):
            S[i] = S[i-1] + A[i-1]

        R = [None] * (N+1)

        for i in range(1,N+1):
            if i == 1:
                R[i] = 0
            else:
                R[i] = R[i-1]
            
            while R[i] < N  and (S[R[i]+1]-S[i-1]) <= K:
                R[i] += 1
        
        ans = 0
        for i in range(1,N+1):
            ans += R[i]-(i-1)
        return ans

