class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        seen = {}

        for i in range(len(names)):
            seen[heights[i]] = names[i]
        

        heights.sort(reverse=True)

        for i in range(len(heights)):
            heights[i] = seen[heights[i]]


        return heights

            