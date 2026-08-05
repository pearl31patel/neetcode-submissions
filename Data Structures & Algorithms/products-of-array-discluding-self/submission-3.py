class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = 1
        r = 1
        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n

        for i in range(len(nums)):
            j = -i-1

            l_arr[i] = l
            r_arr[j] = r

            l = l * nums[i]
            r = r * nums [j]

        res = []

        for i in range(len(nums)):
            res.append(l_arr[i] * r_arr[i])

        return res