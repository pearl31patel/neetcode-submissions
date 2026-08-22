class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            word = "".join(sorted(s))

            if word in d:
                d[word].append(s)
            else:
                d[word] = [s]

        return list(d.values())