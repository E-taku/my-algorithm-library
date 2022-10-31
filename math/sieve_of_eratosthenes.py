# エラトステネスのふるい
# N以下の素数列挙
class Sieve_of_eratosthenes:
    def __init__(self, N: int):
        self.N = N
        # 整数 x が消されている場合に限り Deleted[x]=true
        self.Deleted = [ False ] * 1000009
        LIMIT = int(self.N ** 0.5)

        for i in range(2, LIMIT+1):
            if self.Deleted[i] == False:
                for j in range(i*2, self.N+1, i):
                    self.Deleted[j] = True

        # 素数列挙（リストにまとめる）
        self.prime_list = self.get_prime_enumeration(self.Deleted)

    def get_prime_enumeration(self,deleted: list):
        prime_list = []
        # 素数を列挙する
        for i in range(2, self.N+1):
            if deleted[i] == False:
                prime_list.append(i)
        return prime_list