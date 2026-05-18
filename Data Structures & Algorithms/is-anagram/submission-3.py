from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_d = {}
        t_d = {}

        for i in range(len(s)):
            if s[i] in s_d:
                s_d[s[i]] += 1
            else:
                s_d[s[i]] = 1

            if t[i] in t_d:
                t_d[t[i]] += 1
            else:
                t_d[t[i]] = 1

        return s_d == t_d