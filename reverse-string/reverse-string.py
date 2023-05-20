class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return self.helper(0, len(s)-1, s)
    
    def helper(self, start, end, ls):
        if start >= end:
            return
        
        # swap the first and last element
        ls[start], ls[end] = ls[end], ls[start]        

        return self.helper(start+1, end-1, ls)    
            
        