class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #what im thinking
        #how we can calc. is that the length of the days u see the hottest is the temp at that day
        #pop that out of the stack 

        temp, res = [], [0] * len(temperatures)

        for i in range(len(temperatures)):
            while(temp and temperatures[i] > temp[-1][0]):
                val = temp.pop()
                days = i - val[1]

                res[val[1]] = days
            temp.append([temperatures[i], i])
        return res