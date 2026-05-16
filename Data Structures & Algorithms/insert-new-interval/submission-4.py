class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # res = []
        # i = 0
        # while i < len(intervals):
        #     #add in place
        #     if(newInterval[1] < intervals[i][0]):
        #         res.append(newInterval)
        #         break
        #     elif(newInterval[0] > intervals[i][1]):
        #         res.append(intervals[i])
        #     else:
        #         #newInterval[1] >= intervals[i][0] and newInterval[0] <= intervals[i][1]
        #         newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        #     i += 1
        #     #merge
        
        # #check outside the loop, if our newInterval start is greater then the last intervals end, we append
        # # 2 cases, if adding to the end, or interval already added, appending rest of the arr
        # if not res or newInterval[0] > res[-1][1]:
        #     res.append(newInterval)
        # while i < len(intervals):
        #     res.append(intervals[i])
        #     i += 1
        

        # return res

        #IMPROVED

        res = []
        for i in range(len(intervals)):
            #add in place
            if(newInterval[1] < intervals[i][0]):
                res.append(newInterval)
                return res + intervals[i:]
            elif(newInterval[0] > intervals[i][1]):
                res.append(intervals[i])
            else:
                #newInterval[1] >= intervals[i][0] and newInterval[0] <= intervals[i][1]
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            #merge

        #We know that if we havent already returned, it means interval hasnt been added yet
        res.append(newInterval)

        return res