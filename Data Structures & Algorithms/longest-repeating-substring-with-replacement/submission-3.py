class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        left = 0
        maxWindow = 0
        maxFreq = 0

        for right in range(len(s)):
            idx = ord(s[right])-ord('A')
            freq[idx] += 1

            maxFreq = max(maxFreq,freq[idx])
            window_length = right - left + 1

            if window_length-maxFreq > k:
                left_idx = ord(s[left])-ord('A')
                freq[left_idx] -= 1
                left += 1

            window_length = right - left + 1
            maxWindow = max(maxWindow,window_length)

        return maxWindow
        