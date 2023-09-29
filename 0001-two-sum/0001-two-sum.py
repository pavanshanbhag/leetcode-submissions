class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {} #empty dictionary variable k
        #will be used to store complimnet as Key, and index as value
        for i in range(0,len(nums)):
            cmp = target - nums[i]
            if  nums[i] in d:
                return [d[nums[i]],i]
            d[cmp] = i
        
        print('No such pairs found')
        