class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for s in strs:
            key = "".join(sorted(s))
            if (key in group):
                group[key].append(s)
            else:
                group[key] = [s]
        return list(group.values())
