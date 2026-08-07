class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dups = {} # val : indice


        for i in range(len(nums)):
            if nums[i] in dups:
                if abs(dups[nums[i]] - i) <= k:
                    return True
            dups[nums[i]] = i
        
        return False