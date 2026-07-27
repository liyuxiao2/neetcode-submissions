class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        major = []

        for n in cnt:
            if cnt[n] > len(nums) // 3:
                major.append(n)
        
        return major