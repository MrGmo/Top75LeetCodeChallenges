def two_sum(nums, target):
  prevNumMap = {}
  for i, n in enumerate(nums):
    diff = target-n
    if diff in prevNumMap:
      return [prevNumMap[diff], i]
    prevNumMap[n] = i