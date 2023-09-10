class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # Edge/Boundary Case
        if len(s) != len(t) or len(s)==0 or len(t)==0:
            return False

        s_to_t, t_to_s = {}, {}
        
        for _ in range(len(s)):
            s1, t1=s[_], t[_]

            if s1 in s_to_t and s_to_t[s1]!=t1:
                return False
            else:
                s_to_t[s1]=t1

            if t1 in t_to_s and t_to_s[t1]!=s1:
                return False
            else:
                t_to_s[t1]=s1

        return True