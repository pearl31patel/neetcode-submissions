class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = 1
        r = 1
        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n

        for i in range(n):
            j = -i-1
            l_arr[i] = l
            r_arr[j] = r
            l = l * nums[i]
            r = r * nums[j]

        return [l*r for l,r in zip(l_arr, r_arr)]
        