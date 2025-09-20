
## 1> Reverse Integer
# input = 45673
# output = 37654

def reverse_integer(num):
    return int(str(num)[::-1])


num = 45673
print(reverse_integer(num))


### Without String Conversion (pure math)

def reverse_integers(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10

    return rev


num = 45673
print(reverse_integers(num))


def reverse_negative_integer(x):
    rev = 0
    is_neg = False
    if x < 0:
        is_neg = True
        x = x * -1

    while x > 0:
        rev = rev * 10 + x % 10
        x //= 10

    if rev > 2 ** 31 - 1 : 
        return 0
    return rev * -1 if is_neg else rev

num = 45673
print(reverse_negative_integer(num))


## 2> palindrome number
# input : 121
# output : True

def palindrome_number(num):
    temp = num
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    
    return True if temp == rev else False


num = 121
print(palindrome_number(num))

# 3. Sum of Digits
# input : 987
# output : 24

def sum_of_digit(num):
    
    digit_sum = 0
    while num > 0:
        digit_sum = digit_sum + num % 10
        num //= 10
    
    return digit_sum
    

num = 987
print(sum_of_digit(num))

## 4. Count Digits
# Input: 45673 → Output: 5.

def count_digit(num):
    digit_cnt = 0
    while num > 0:
        digit_cnt += 1
        num //= 10
    
    return digit_cnt

num = 45673
print(count_digit(num))

## 5. Product of Digits
# Input: 234 → Output: 2*3*4 = 24.

def product_digit(num):

    product = 1
    while num > 0:
        product *= num % 10
        num //= 10
    
    return product

num = 234
print(product_digit(num))


## 6. Armstrong Number / Narcissistic Number
# Input: 153 = 1³ + 5³ + 3³ → Output: True.

def armstrong_number(num):
    temp = num
    res = 0
    n = len(str(num))

    while num > 0:
        r = num % 10
        res += r ** n
        num //= 10
    
    return True if temp == res else False

num = 153
print(armstrong_number(num))


## 7. Factorial of a Number
# Input: 5 → Output: 120.

def factorial_number(num):
    if num <=0:
        return 0
    res = 1
    while num > 1:
        res *= num
        num -= 1 

    return res

num = 5
print(factorial_number(num))

# recursive 
def factorial_recursive(num):
    if num < 0:
        return None
    if num == 0:
        return 1
    return num * factorial_recursive(num- 1)

num = 5
print(factorial_recursive(num))


## 8. Prime Check
# Input: 29 → Output: True.

def prime_number(num):
    flag = False

    if num <=1:
        return False
    
    if num <= 3:
        return True

    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
        
    return False if flag else True

num = 29
print(prime_number(num))


## 9. GCD / LCM of Two Numbers
# Input: (12, 18) → GCD = 6, LCM = 36.

def gcd_lcm_of_number(num):
    a, b = num

    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    gcd_val = gcd(a,b)
    lcd_val = abs(a*b) // gcd_val
    
    return f"GCD:{gcd_val},LCM: {lcd_val}"

num = (12, 18)
print(gcd_lcm_of_number(num))


## 10. Fibonacci Numbers
# Input: n=6 → Sequence: 0, 1, 1, 2, 3, 5.

def fibonacci_number_sequence(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    
    seq = [0, 1]

    for i in range(2, num):
        seq.append(seq[-1]+seq[-2])
    
    return seq


num = 6
print(fibonacci_number_sequence(num))


def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

def fibonacci_number_recursive(num):
        return [fib_recursive(i) for i in range(num)]


num = 6
print(fibonacci_number_recursive(num))

# Input: n=6 → output: 0, 1, 1, 2, 3, 5.
def fibonacci_number(num: int) -> int:
    if num <= 0:
        return 0
    elif num == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, num + 1):
        a, b = b, a + b
    return b

num = 6
print(fibonacci_number(num))


## 11. Happy Number
# Replace number by sum of squares of digits until it becomes 1 (happy) or loops endlessly (sad).
# Input: 19 → Output: True

def happy_number(num):
    seen = set()

    while num != 1 and num not in seen:
        seen.add(num)
        num = sum((int(digit) ** 2 for digit in str(num)))
    return num == 1

num = 19
print(happy_number(num))



## 12. Power of Two / Three / Four
# Check if number can be expressed as 2^n, 3^n, or 4^n.
# Input: 16 → True (LeetCode 231, 326, 342).

def power_of_number(power, num):

    while num % power == 0:
        num //= power

    return num ==1


num = 16
power = 2
# power = 3
# power = 4

print(power_of_number(power, num))


## 13. Integer Square Root
# Input: 8 → Output: 2 (floor of √8).
                      


## 14. Integer to Roman / Roman to Integer
# Input: 58 → Output: "LVIII"
# Input: "MCMXCIV" → Output: 1994

def integer_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]
    res = ""

    for i in range(len(val)):
        while num >= val[i]:
            res += syms[i]
            num -= val[i]
    return res

num = 58 
print(integer_to_roman(num))


def roman_to_integer(st):
    roman = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }
    res = 0
    i = 0
    while i < len(st):
        if i + 1 < len(st) and roman[st[i]] < roman[st[i+1]]:
            res += roman[st[i+1]] - roman[st[i]]
            i += 2
        else:
            res += roman[st[i]]
            i += 1
    
    return res


word = "MCMXCIV"
print(roman_to_integer(word))



#15. Reverse Bits
# Input: 00000010100101000001111010011100
# Output: 964176192


#3 16. Counting Bits
# Input: 5 → Output: [0,1,1,2,1,2] (# of 1s in binary representation)
    

## 17. Hamming Distance
# Count differing bits between two numbers.
# Input: (1,4) → Output: 2


## 18. Bitwise Single Number Problems
# Find unique numbers where all others appear twice or thrice.
# Input: [2,2,1] → Output: 1


## 19. Integer Division without Using Operators
# Implement division without /, *, or %.
# Input: 10 / 3 → Output: 3



## 20. Excel Sheet Column Title / Number
# Convert integer to Excel column title.
# Input: 28 → Output: "AB"


## 21. Ugly Numbers
# Numbers whose only prime factors are 2, 3, or 5.
# Input: 6 → Output: True


## 22. Super Pow (a^b mod 1337)
# Exponentiation by squaring with big powers


## 23. Add Digits
# Repeated digit sum until one digit remains.
# Input: 38 → Output: 2



## 24. Integer Break
# Split integer into sum of ≥2 positive integers, maximize product.
# Input: 10 → Output: 36


## 25. Perfect Number
# Sum of divisors equals number.
# Input: 28 → Output: True.