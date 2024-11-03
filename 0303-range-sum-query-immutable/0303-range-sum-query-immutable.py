class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = [0]
        
        for idx in range(len(nums)):
            prev = self.prefix_sum[-1]
            if idx == len(self.prefix_sum)-1:
                self.prefix_sum[idx] = prev + nums[idx]
            else :
                self.prefix_sum.append(prev + nums[idx])

        

    def sumRange(self, left: int, right: int) -> int:
        if left>0 and right>0:
            return self.prefix_sum[right] - self.prefix_sum[left-1]
        else :
            return self.prefix_sum[left or right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)