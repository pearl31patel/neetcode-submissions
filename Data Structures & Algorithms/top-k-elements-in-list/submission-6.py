class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1

        bucket = []

        for i in range(len(nums)+1):
            bucket.append([])

        for num,count in d.items():
            bucket[count].append(num)

        res = []

        for i in range(len(bucket)-1,-1,-1):
            for num in bucket[i]:
                res.append(num)

                if len(res) == k:
                    return res

                



