'''Given two strings ransomNote and magazine, return true
if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.'''
# def canConstruct(ransomNote: str, magazine: str):
#     ran = list(ransomNote)
#     mag = list(magazine)
#     for i in ran:
#         if i in mag:
#             mag.remove(i)
#         else:
#             return False
#     return True

def reverse(x: int) -> int:
    if x <= pow(-2, 31) or x >= (pow(2, 31) - 1):
        return 0
    flag = False
    if x < 0:
        flag = True
    x = abs(x)
    num = x
    res = 0
    suma = 0
    while num != 0:
        num = num // 10
        res += 1
    while x != 0:
        if x % 10 == 0:
            x = x // 10
            res -= 1
            continue
        suma += (x % 10) * pow(10, res - 1)
        res -= 1
        x = x // 10
    if flag == True:
        return -suma
    return suma

print(reverse(1534236469))
print(pow(2, 31) - 1)