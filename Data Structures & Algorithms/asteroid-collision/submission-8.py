class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        collisions = [asteroids[0]]

        for asteroid in asteroids[1:]:
            alive = True
            while collisions and asteroid < 0 and collisions[-1] > 0:
                if collisions[-1] < abs(asteroid):
                    collisions.pop()
                    continue
                elif collisions[-1] == abs(asteroid):
                    collisions.pop()
                    alive = False
                    break
                else:
                    alive = False
                    break
            if alive:
                collisions.append(asteroid)
        return collisions