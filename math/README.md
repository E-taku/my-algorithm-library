## Math
|File Name|Algorithm|computational complexity|Explanation|
|:--:|:--:|:--:|:--:|
|[isPrime.py](isPrime.py)|素数判定|計算量O(√N)|すべての合成数は<br>２以上√N以下の約数をもつ
|[sieve_of_eratosthenes.py](sieve_of_eratosthenes.py)|エラトステネスの篩<br>素数列挙|計算量O(N log log N)|N以下の素数を高速に列挙する
|[gcd_lcm.py](gcd_lcm.py)|最大公約数<br>最小公倍数|計算量O( log(a+b) )　|２値の最大公約数、最小公倍数を求める<br>ユークリッドの互除法を用いる
|[power.py](power.py)|累乗（余りの計算）|計算量O() | a^bをMODで割った余りを求める<br> 1<=a<=10^9,1<=b<=10^18 に対応可