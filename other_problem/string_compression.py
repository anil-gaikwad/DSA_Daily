from collections import Counter

######################  1. STRING COMPRESSION  ######################
# Input:  "weelllcoomee"
# Output: "we2l3co2me2"

def string_compression(word):
    res, cnt = [], 1

    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            cnt += 1
        else:
            res.append(word[i - 1] + (str(cnt) if cnt > 1 else ""))
            cnt = 1

    res.append(word[-1] + (str(cnt) if cnt > 1 else ""))
    return "".join(res)


######################  2. STRING DECOMPRESSION  ######################
# Input:  "a3b2cd3"
# Output: "aaabbcddd"

def string_decompression(word):
    res, i = [], 0

    while i < len(word):
        char = word[i]
        i += 1
        num = ""

        # Collect multi-digit numbers
        while i < len(word) and word[i].isdigit():
            num += word[i]
            i += 1

        res.append(char * int(num) if num else char)

    return "".join(res)


######################  3. STRING ENCODING  ######################
# Input:  "abababab"
# Output: "4[ab]"

# Approach 1: Divisor check
def string_encoding_1(word):
    n = len(word)
    for size in range(1, n // 2 + 1):
        if n % size == 0:
            pattern = word[:size]
            if pattern * (n // size) == word:
                return f"{n // size}[{pattern}]"
    return word

# Approach 2: Using word+word trick
def string_encoding_2(word):
    n = len(word)
    idx = (word + word).find(word, 1)

    if idx != -1 and idx < n:
        repeat = n // idx
        return f"{repeat}[{word[:idx]}]"
    return word


######################  DEMO  ######################
if __name__ == "__main__":
    # Compression
    print("Compression:")
    print(string_compression("weelllcoomee"))   # we2l3co2me2
    print(string_compression("abc"))            # abc
    print(string_compression("aaaa"))           # a4

    # Decompression
    print("\nDecompression:")
    print(string_decompression("a3b2cd3"))      # aaabbcddd
    print(string_decompression("a10b3"))        # aaaaaaaaaabb bbb
    print(string_decompression("xyz"))          # xyz

    # Encoding
    print("\nEncoding:")
    print(string_encoding_1("abababab"))        # 4[ab]
    print(string_encoding_1("abcabcabc"))       # 3[abc]
    print(string_encoding_1("abcd"))            # abcd

    print(string_encoding_2("abababab"))        # 4[ab]
    print(string_encoding_2("abcabcabc"))       # 3[abc]
    print(string_encoding_2("abcd"))            # abcd
