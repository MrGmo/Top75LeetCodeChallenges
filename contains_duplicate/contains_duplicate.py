def containsDuplicate(nums):
    prevObj = {}
    for char in nums:
        if char in prevObj:
            return True
        prevObj[char] = 1
    return False
