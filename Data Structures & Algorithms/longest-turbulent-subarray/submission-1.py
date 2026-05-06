class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1

        l, r = 0, 1
        res, prev = 0, ""

        while r < len(arr):
            if arr[r - 1] < arr[r] and prev == "<":
                l = r - 1
            elif arr[r - 1] > arr[r] and prev == ">":
                l = r - 1
            elif arr[r - 1] == arr[r]:
                l = r

            if arr[r - 1] < arr[r]:
                prev = "<"
            elif arr[r - 1] > arr[r]:
                prev = ">"
            else:
                prev = "="

            res = max(res, r - l + 1)
            r+=1
        return res

        # 2,4,3,2,2,5,1,4
        # l.    r

        # <