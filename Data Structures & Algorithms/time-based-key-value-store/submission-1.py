class TimeMap:

    def __init__(self):
        self.hashmap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        
        arr = self.hashmap[key]
        l,r = 0, len(arr)-1
        res = ""

        while l <= r:
            m = (l+r)//2
            num = arr[m][0]

            if num <= timestamp:
                res = arr[m][1]
                l = m + 1
            else:
                r = m - 1
        return res


        # res=4
        # 1,2,3,4 target = 5
        #   |
        #     |
        #       |

        # res = 2
        # 1,2,4,5 target = 3
        #   |
        #     |

        # 10  target = 1
        # |