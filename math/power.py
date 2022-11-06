# a の b 乗を m で割った余りを返す
class Power:
    def __init__(self,a: int,b: int,mod: int) -> None:
        self.a = a
        self.b = b
        self.mod = mod
        self.ans = self.get_power()

    def get_power(self) -> int:
        ans = 1
        b_bin = bin(self.b)[2:]

        A = [None] * (len(b_bin))
        A[0] = self.a
        for i in range(1,len(b_bin)):
            A[i] = (A[i-1] *  A[i-1]) % self.mod

        i = 0
        for c in reversed(b_bin):
            if c == '1':
                ans = (ans * A[i]) % self.mod
            i += 1
        return ans