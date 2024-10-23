class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target = abs(target)
        maximum = sum(nums)
        if maximum < target:
            return 0
        if maximum == target:
            return 2 ** nums.count(0)
        minimum = - (maximum // 2)
        length = maximum - minimum

        prev = [0] * (length)
        curr = [0] * (length)

        # one way to make a sum of 0 with no elements
        prev[0] = 1
        for num in nums:
            # loop indices so that any index accessed is in the range [minimum:maximum+1]
            for t in range(maximum - num, minimum-1, -1):
                curr[t+num] += prev[t]
            for t in range(maximum, minimum-1+num, -1):
                curr[t-num] += prev[t]
            prev = curr
            curr = [0] * (length)
        
        return prev[target]
        