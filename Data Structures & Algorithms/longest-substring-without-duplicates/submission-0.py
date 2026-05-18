class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLength = 0
        h = set()

        for right in range(len(s)):

            while s[right] in h:
                h.remove(s[left])
                left += 1

            h.add(s[right])
            maxLength = max(maxLength,right - left + 1)

        return maxLength
       


        