class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = current_max = current_min = prev_max = prev_min = nums[0]

        for num in nums[1:]:
            current_max = max(num, num*prev_max, num*prev_min)
            current_min = min(num, num*prev_max, num*prev_min)
            ans = max(ans, current_max)
            prev_max, prev_min = current_max, current_min

        return ans 
        