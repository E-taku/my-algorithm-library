# 最大公約数（GCD)と最小公倍数（LCM）

class Gcd_Lcm:
    def __init__(self,a: int,b: int) -> None:
        self.a = a
        self.b = b
        self.gcd = self.get_GCD(self.a, self.b)
        self.lcm = self.get_LCM(self.a, self.b)

    # 2値の最大公約数を求める
    def get_GCD(self, a: int, b: int) -> int:
        while a >= 1 and b >= 1:
            if a >= b:
                a = a % b
            else:
                b = b % a
        if a != 0:
            return a
        return b

    # 2値の最小公倍数を求める
    def get_LCM(self, a: int, b: int) -> int:
        lcm = (a * b) // self.gcd
        return lcm