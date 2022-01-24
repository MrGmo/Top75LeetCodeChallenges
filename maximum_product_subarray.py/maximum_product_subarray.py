def maxProduct(self, nums):
    res = max(nums)
    currentMin, currentMax = 1, 1
    for n in nums:
        temp = currentMax * n
        currentMax = max(n * currentMax, n * currentMin, n)
        currentMin = min(temp, n * currentMin, n)
        res = max(res, currentMax)
    return res
