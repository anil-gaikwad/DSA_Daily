## 2> string compression
# word = "weelllcoomee"
# output = "we2l3co2me2"

def string_compression(word):
    res = []
    cnt = 1

    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            cnt += 1
        else:
            res.append(word[i - 1] + (str(cnt) if cnt > 1 else ""))
            cnt = 1

    res.append(word[-1] + (str(cnt) if cnt > 1 else ""))
    return "".join(res)

word = "weelllcoomee"
print(string_compression(word))

## string decompresssion 
# Input:  "a3b2cd3"  
# Output: "aaabbcddd"

def string_decompresssion(word):
    res = []
    i = 0

    while i < len(word):
        char = word[i]
        i += 1
        num = ""

        if i < len(word) and word[i].isdigit():
            num += word[i]
            i += 1
        
        if num:
            res.append(char * int(num))
        else:
            res.append(char)
    
    return "".join(res)
                
word = "a3b2cd3"
print(string_decompresssion(word=word))


## 3> string encoding
# Input:  "abababab"  
# Output: "4[ab]"

def string_encoding_1(word):
    n = len(word)
    
    for size in range(1, n // 2 +1):
        if n % size == 0:
            pattern = word[:size]
            if pattern * (n // size) == word:
                return f"{n//size}[{pattern}]"


    return word

word = "abababab"
print(string_encoding_1(word))


def string_encoding_2(word):
    n = len(word)

    idx = (word + word).find(word, 1)
    print((word + word))
    print(idx)
    if idx != -1 and idx < n :
        repeat = n // idx
        return f"{repeat}[{word[:idx]}]"
    
    return word

word = "abababab"
print(string_encoding_2(word))


