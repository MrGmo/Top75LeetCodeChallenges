# Time: O(n), Space: O(1)
def maxArea(self, height):
    max_area = 0
    l, r = 0, len(height) - 1

    while l < r:
        area = (r - l) * min(height[l], height[r])
        max_area = max(area, max_area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area
