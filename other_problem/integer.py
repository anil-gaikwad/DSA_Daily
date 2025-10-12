# ============================================================
# 1. Reverse Integer
# Input: 45673 → Output: 37654
# ============================================================
def reverse_integer(num: int) -> int:
    return int(str(num)[::-1])

print(reverse_integer(45673))  # 37654


def reverse_integer_math(num: int) -> int:
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

print(reverse_integer_math(45673))  # 37654


def reverse_integer_with_sign(num: int) -> int:
    rev, sign = 0, -1 if num < 0 else 1
    num = abs(num)
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return 0 if rev > 2**31 - 1 else rev * sign

print(reverse_integer_with_sign(45673))  # 37654


# ============================================================
# 2. Palindrome Number
# Input: 121 → Output: True
# ============================================================
def is_palindrome_number(num: int) -> bool:
    temp, rev = num, 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return temp == rev

print(is_palindrome_number(121))  # True


# ============================================================
# 3. Sum of Digits
# Input: 987 → Output: 24
# ============================================================
def sum_of_digits(num: int) -> int:
    s = 0
    while num > 0:
        s += num % 10
        num //= 10
    return s

print(sum_of_digits(987))  # 24


# ============================================================
# 4. Count Digits
# Input: 45673 → Output: 5
# ============================================================
def count_digits(num: int) -> int:
    cnt = 0
    while num > 0:
        cnt += 1
        num //= 10
    return cnt

print(count_digits(45673))  # 5


# ============================================================
# 5. Product of Digits
# Input: 234 → Output: 24
# ============================================================
def product_of_digits(num: int) -> int:
    prod = 1
    while num > 0:
        prod *= num % 10
        num //= 10
    return prod

print(product_of_digits(234))  # 24


# ============================================================
# 6. Armstrong Number
# Input: 153 → Output: True
# ============================================================
def is_armstrong_number(num: int) -> bool:
    temp, res = num, 0
    n = len(str(num))
    while num > 0:
        res += (num % 10) ** n
        num //= 10
    return temp == res

print(is_armstrong_number(153))  # True


# ============================================================
# 7. Factorial
# Input: 5 → Output: 120
# ============================================================
def factorial_iterative(num: int) -> int:
    if num < 0:
        return None
    res = 1
    while num > 1:
        res *= num
        num -= 1
    return res

print(factorial_iterative(5))  # 120


def factorial_recursive(num: int) -> int:
    if num < 0:
        return None
    return 1 if num == 0 else num * factorial_recursive(num - 1)

print(factorial_recursive(5))  # 120


# ============================================================
# 8. Prime Check
# Input: 29 → Output: True
# ============================================================
def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(29))  # True


# ============================================================
# 9. GCD and LCM
# Input: (12, 18) → Output: (6, 36)
# ============================================================
def gcd_lcm(a: int, b: int):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    g = gcd(a, b)
    l = abs(a * b) // g
    return g, l

print(gcd_lcm(12, 18))  # (6, 36)


# ============================================================
# 10. Fibonacci
# Input: n=6 → Output: [0,1,1,2,3,5]
# ============================================================
def fibonacci_sequence(n: int):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

print(fibonacci_sequence(6))  # [0,1,1,2,3,5]


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_sequence(n):
    return [fibonacci(i) for i in range(n)]

print(fibonacci_sequence(6))  # [0, 1, 1, 2, 3, 5]


# ============================================================
# 11. Happy Number
# Input: 19 → Output: True
# ============================================================
def is_happy_number(num: int) -> bool:
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(d) ** 2 for d in str(num))
    return num == 1

print(is_happy_number(19))  # True


# ============================================================
# 12. Power of N
# Input: (2,16) → Output: True
# ============================================================
def is_power_of(n: int, num: int) -> bool:
    if num <= 0:
        return False
    while num % n == 0:
        num //= n
    return num == 1

print(is_power_of(2, 16))  # True


# ============================================================
# 13. Integer Square Root
# Input: 8 → Output: 2
# ============================================================
def integer_square_root(num: int) -> int:
    return int(num ** 0.5)

print(integer_square_root(8))  # 2


# ============================================================
# 14. Roman ↔ Integer
# Input: 58 → "LVIII", "MCMXCIV" → 1994
# ============================================================
def integer_to_roman(num: int) -> str:
    val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    syms = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    res = ""
    for i in range(len(val)):
        while num >= val[i]:
            res += syms[i]
            num -= val[i]
    return res

print(integer_to_roman(58))  # LVIII


def roman_to_integer(s: str) -> int:
    roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    res, i = 0, 0
    while i < len(s):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
            res += roman[s[i+1]] - roman[s[i]]
            i += 2
        else:
            res += roman[s[i]]
            i += 1
    return res

print(roman_to_integer("MCMXCIV"))  # 1994


# ============================================================
# 15. Reverse Bits
# ============================================================
def reverse_bits(n: int, bits=32) -> int:
    res = 0
    for _ in range(bits):
        res = (res << 1) | (n & 1)
        n >>= 1
    return res

print(reverse_bits(0b00000010100101000001111010011100))


# ============================================================
# 16. Counting Bits
# Input: 5 → [0,1,1,2,1,2]
# ============================================================
def counting_bits(n: int):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp

print(counting_bits(5))


# ============================================================
# 17. Hamming Distance
# Input: (1,4) → Output: 2
# ============================================================
def hamming_distance(x: int, y: int) -> int:
    return bin(x ^ y).count("1")

print(hamming_distance(1, 4))


# ============================================================
# 18. Single Number
# Input: [2,2,1] → Output: 1
# ============================================================
def single_number(nums) -> int:
    res = 0
    for n in nums:
        res ^= n
    return res

print(single_number([2, 2, 1]))


# ============================================================
# 19. Division without Operators
# Input: 10 / 3 → Output: 3
# ============================================================
def divide(dividend: int, divisor: int) -> int:
    if divisor == 0:
        raise ZeroDivisionError
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
    dividend, divisor = abs(dividend), abs(divisor)
    quotient = 0
    while dividend >= divisor:
        temp, multiple = divisor, 1
        while dividend >= (temp << 1):
            temp <<= 1
            multiple <<= 1
        dividend -= temp
        quotient += multiple
    return max(min(sign * quotient, 2**31 - 1), -2**31)

print(divide(10, 3))  # 3


# ============================================================
# 20. Excel Column ↔ Number
# ============================================================
def number_to_excel(n: int) -> str:
    res = ""
    while n > 0:
        n -= 1
        res = chr(n % 26 + ord("A")) + res
        n //= 26
    return res

print(number_to_excel(28))  # AB


def excel_to_number(s: str) -> int:
    res = 0
    for c in s:
        res = res * 26 + (ord(c) - ord("A") + 1)
    return res

print(excel_to_number("AB"))  # 28


# ============================================================
# 21. Ugly Number
# ============================================================
def is_ugly(num: int) -> bool:
    if num <= 0:
        return False
    for p in [2, 3, 5]:
        while num % p == 0:
            num //= p
    return num == 1

print(is_ugly(6))   # True
print(is_ugly(14))  # False


# ============================================================
# 22. Super Pow
# ============================================================
MOD = 1337
def super_pow(a: int, b: list) -> int:
    if not b:
        return 1
    last = b.pop()
    return (pow(super_pow(a, b), 10, MOD) * pow(a, last, MOD)) % MOD

print(super_pow(2, [1,0]))  # 1024 % 1337 = 1024


# ============================================================
# 23. Add Digits
# Input: 38 → Output: 2
# ============================================================
def add_digits(num: int) -> int:
    return 1 + (num - 1) % 9 if num > 0 else 0

print(add_digits(38))  # 2


# ============================================================
# 24. Integer Break
# Input: 10 → Output: 36
# ============================================================
def integer_break(n: int) -> int:
    if n <= 3:
        return n - 1
    product = 1
    while n > 4:
        product *= 3
        n -= 3
    return product * n

print(integer_break(10))  # 36


# ============================================================
# 25. Perfect Number
# Input: 28 → Output: True
# ============================================================
def is_perfect_number(num: int) -> bool:
    if num <= 1:
        return False
    s = 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            s += i
            if i != num // i:
                s += num // i
    return s == num

print(is_perfect_number(28))  # True
