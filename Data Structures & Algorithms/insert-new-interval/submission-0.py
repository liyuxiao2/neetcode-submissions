class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        while i < len(intervals):
            #add in place
            if(newInterval[1] < intervals[i][0]):
                res.append(newInterval)
                break
            elif(newInterval[0] > intervals[i][1]):
                res.append(intervals[i])
            else:
                #newInterval[1] >= intervals[i][0] and newInterval[0] <= intervals[i][1]
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
            #merge
        
        #check outside the loop, if our newInterval start is greater then the last intervals end, we append
        print(res)
        # 2 cases, if adding to the end, or interval already added, appending rest of the arr
        if not res or newInterval[0] > res[-1][1]:
            res.append(newInterval)
        elif i < len(intervals):
            res = res + intervals[i:]
        

        return res