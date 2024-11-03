class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg, window_avg, window_sum, window_start = float('-inf'), 0, 0, 0
        
        # Edge case - n < k : no need to handle as constraint clearly specifies that k <= n
        # Edge case - empty string : no need to handle

        for window_end in range(len(nums)):
            window_sum += nums[window_end] # add the element

            # slide the window when size is reached to k 
            if window_end >= k-1 : 
                window_avg =  window_sum/k
                max_avg = max(max_avg, window_avg)
                window_sum -= nums[window_start] # remove the element going out
                window_start += 1 # slide the window ahead
        
        return max_avg
                