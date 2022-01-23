def maxSubArray(nums):
    max_sub = nums[0]
    temp_sum = 0
    for n in nums:
        if temp_sum < 0:
            temp_sum = 0
        temp_sum += n
        max_sub = max(max_sub, temp_sum)
    return max_sub
