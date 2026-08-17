class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = "-999"

        for i in range(len(num[:-2])):
            if num[i] == num[i+1] == num[i+2] and int(num[i: i + 3]) >= int(largest):
                largest = num[i: i + 3]
        
        print(largest)
        
        return str(largest) if largest != "-999" else ""