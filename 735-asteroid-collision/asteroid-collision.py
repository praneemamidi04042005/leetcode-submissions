class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        l=[]
        for i in asteroids:
            if i > 0:
                l.append(i)
            if i < 0:
                # FIX 1: Change condition to check if stack has RIGHT-moving asteroids
                while l and l[-1] > 0 and l[-1] < abs(i):
                    l.pop()
                
                # FIX 2: Handle if both are equal size
                if l and l[-1] > 0 and l[-1] == abs(i):
                    l.pop()
                elif not l or l[-1] < 0:
                    l.append(i)
        return l