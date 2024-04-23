class TimeMap:

    def __init__(self):
        self.store = {} # key : list of [val, timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        # print(self.store)

    def get(self, key: str, timestamp: int) -> str:
        val = self.store.get(key,[]) # return empty list if key do not exist.
        res = ""
        l = 0
        r = len(val) - 1
        while(l <= r):
            m = (l + r) // 2
            if val[m][1] <= timestamp:
                res = val[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo", "bar", 1)
assert obj.get("foo", 1) == "bar"
assert obj.get("foo", 3) == "bar"
obj.set("foo", "bar2", 4) 
assert obj.get("foo", 4) == "bar2"
assert obj.get("foo", 5) == "bar2"