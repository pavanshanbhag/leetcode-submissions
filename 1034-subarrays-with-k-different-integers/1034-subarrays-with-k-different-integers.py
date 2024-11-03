class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most_k(arr, k):
            count = Counter()
            left = 0
            result = 0
            for right in range(len(arr)):
                if count[arr[right]] == 0:
                    k -= 1
                count[arr[right]] += 1
                while k < 0:
                    count[arr[left]] -= 1
                    if count[arr[left]] == 0:
                        k += 1
                    left += 1
                result += right - left + 1
            return result

        return at_most_k(nums, k) - at_most_k(nums, k - 1) 
                




