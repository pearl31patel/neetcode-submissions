class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        left = 0
        maxLength = 0

        for right in range(len(s)):

            while s[right] in hashSet:
                hashSet.remove(s[left])
                left += 1

            hashSet.add(s[right])
            maxLength = max(maxLength,right-left+1)

        return maxLength