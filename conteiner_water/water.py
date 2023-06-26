def maxArea(height) -> int:
    start = 0
    end = len(height) - 1
    ans = 0
    while start < end:
        temp = min(height[start], height[end]) * (end - start)
        if temp > ans:
            ans = temp
        if height[start] >= height[end]:
            end -= 1
        else:
            start += 1

    return ans





print(maxArea([1,8,6,2,5,4,8,3,7]))

