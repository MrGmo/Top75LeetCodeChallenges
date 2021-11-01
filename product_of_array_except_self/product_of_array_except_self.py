def product_except_self(nums):
    result_list = [1]*(len(nums))
    prefix = 1
    for i in range(len(nums)):
        result_list[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        result_list[i] *= postfix
        postfix *= nums[i]
    return result_list