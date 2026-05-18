class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}

        for n in strs:
            word = "".join(sorted(n))
            if word in d:
                d[word].append(n)
            else:
                d[word] = [n]

        return list(d.values())