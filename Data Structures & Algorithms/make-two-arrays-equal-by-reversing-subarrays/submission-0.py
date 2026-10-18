class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        counter = Counter(target)

        for i in range(len(arr)):
            if arr[i] not in counter:
                return False
            if counter[arr[i]] > 0:
                counter[arr[i]] -= 1

                if counter[arr[i]] == 0:
                    counter.pop(arr[i])
        
        return True
