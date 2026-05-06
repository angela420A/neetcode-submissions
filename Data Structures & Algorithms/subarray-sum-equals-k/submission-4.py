class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixMap = { 0 : 1 } # key: prefix sum, value: count
        res = 0
        currNum = 0

        for n in nums:
            currNum += n

            diff = currNum - k
            res += 0 if diff not in prefixMap else prefixMap[diff]
            prefixMap[currNum] = 1 + prefixMap.get(currNum, 0)
        return res