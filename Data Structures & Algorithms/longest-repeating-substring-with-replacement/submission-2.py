class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        arr = [0] * 26
        left = 0
        maxWindow = 0
        maxFreq = 0

        for right in range(len(s)):
            temp = ord(s[right]) - ord('A')
            arr[temp] += 1

            maxFreq = max(maxFreq,arr[temp])
            windowLength = right - left + 1

            if(windowLength - maxFreq > k):
                arr[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            windowLength = right - left + 1
            maxWindow = max(maxWindow,windowLength)

        return maxWindow
