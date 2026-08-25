class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        maps = {}

        for i in range(len(nums2)):
            j = i + 1

            while j < len(nums2) and nums2[i] > nums2[j]:
                j += 1
            
            maps[nums2[i]] = nums2[j] if j < len(nums2) else -1

        

        for i in range(len(nums1)):
            nums1[i] = maps[nums1[i]]

        print(maps)
        return nums1

                
