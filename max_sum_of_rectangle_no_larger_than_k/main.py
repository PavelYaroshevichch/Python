import math
# def maxSumSubmatrix(matrix, k: int) -> int:
#     m = n = 0
#     for i in matrix:
#         m += 1
#     n = len(matrix[0])
#
#
# print(maxSumSubmatrix([[1,0,1],[0,-2,3]], 2))def longestCommonPrefix(self, strs: List[str]) -> str:
#         res = ''
#         i = -1
#         j = 0
#         while i < len(strs[0]):
#             i += 1
#             while j < len(strs):
#                 if strs[0][i] == strs[j][i]:
#                     j += 1
#                 else:
#                     return res
#                 res += strs[0][i]
#         return res
def longestCommonPrefix(strs) -> str:
    res = ''
    i = 0
    j = 0
    strs = sorted(strs, key=len)
    while i < len(strs[0]):
        while j < len(strs):
            if strs[0][i] == strs[j][i]:
                j += 1
            else:
                return res
        j = 0
        res += strs[0][i]
        i += 1
    return res
print(longestCommonPrefix(["flower","flow","flight"]))
print(len(['']))
print(math.log(((1 << 31) - 1), 3))
print(pow(3, 19))