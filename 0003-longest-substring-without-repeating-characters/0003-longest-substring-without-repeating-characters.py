class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start, char_freq, max_len = 0, {}, 0
        # Edge case - handle when string is empty
        if not s :
            return max_len
        # Edge case - handle when its just one character
        # if len(s) < 2:
        #     return len(s)

        for window_end in range(len(s)):
            char = s[window_end]
            if char not in char_freq:
                char_freq[char] = 1
                max_len = max(max_len, len(char_freq))
            else:
                while char in char_freq:
                    del char_freq[s[window_start]]  # element going out
                    window_start += 1
                char_freq[char] = 1 # insert it as new char
        

        return max_len
                
