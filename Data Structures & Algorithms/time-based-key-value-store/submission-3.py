class TimeMap:

    def __init__(self):
        self.key_map = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.key_map:
            self.key_map[key].append((value, timestamp))
        else:
            self.key_map[key] = [(value,timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.key_map:
            res = ""
            search_list = self.key_map[key]
            l, r = 0, len(search_list) - 1

            while l <= r:
                middle = (l + r) // 2

                search_time = search_list[middle][1]

                if search_time <= timestamp:
                    res = search_list[middle][0]
                    l = middle + 1
                else:
                    r = middle - 1

            return res
        else:
            return ""

        
