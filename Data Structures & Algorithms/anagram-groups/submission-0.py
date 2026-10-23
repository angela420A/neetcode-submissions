class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for w in s:
                count[ord(w) - ord('a')] += 1
            maps[tuple(count)].append(s)
        return list(maps.values())