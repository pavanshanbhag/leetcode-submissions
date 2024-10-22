class Solution:
    def kadane(self, nums):
        local_max = global_max = nums[0]
        for num in nums[1:]:
            local_max = max(num, num+local_max)
            if local_max > global_max:
                global_max = local_max
        return global_max

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Case 1
        kadane_max = self.kadane(nums)

        wrap_sum = sum(nums)
        # Case 2
        for i in range(len(nums)):
            nums[i] = -nums[i]
        kadane_inverted_max = self.kadane(nums)

        wrap_sum = wrap_sum + kadane_inverted_max

        if wrap_sum == 0:
            return kadane_max
        return max(kadane_max, wrap_sum)
        