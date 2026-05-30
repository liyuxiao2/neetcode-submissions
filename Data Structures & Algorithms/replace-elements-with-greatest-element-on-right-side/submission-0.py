class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        cur_max = maximum = -1

        for i in range(len(arr) - 1, -1, -1):
            print(cur_max)
            if arr[i] > cur_max:
                cur_max = arr[i]
            
            arr[i] = maximum
            maximum = cur_max
            

        
        return arr
