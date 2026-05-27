from collections import defaultdict
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        inventory = defaultdict(int)

        for bill in bills:
            match bill:
                case 5:
                    inventory[5] += 1 
                case 10:
                    if inventory.get(5,0) == 0:
                        return False
                    else:
                        inventory[5] -= 1
                        inventory[10] += 1
                case 20:
                    print(inventory.get(5,0), inventory.get(10,0))
                    if inventory.get(5, 0) < 3 and (inventory.get(10, 0) < 1 or inventory.get(5, 0) < 1):
                        return False
                    elif inventory.get(5) >= 3:
                        inventory[5] -= 3
                    else:
                        inventory[5] -= 1
                        inventory[10] -= 1
        print(inventory)
                        
        return True

            