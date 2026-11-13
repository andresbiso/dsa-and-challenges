"""
Problem: 292.Nim Game
https://leetcode.com/problems/nim-game/
"""
class Solution:
    def canWinNim(self, n: int) -> bool:
        if n <= 3:
            return True
        return n % 4 != 0

solution = Solution()
print(solution.canWinNim(8)) 

"""
My Notes:
I always go first.
If 1 to 3 stones then I win.
>= 4 is when I need to determine if I can win.
If it is a multiple of 4 then I always lose. No matter how many stones I take first.
"""