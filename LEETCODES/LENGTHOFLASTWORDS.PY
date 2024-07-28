class Solution:
    def lengthOfLastWord(self, s: str) -> int:
         # Trim trailing spaces
         # s = s.rstrip()
        words = s.split()
        if not words:
            return 0
        return len(words[-1])

# Create an instance of Solution
sol = Solution()
print(sol.lengthOfLastWord("Hello World")) # Output: 5
print(sol.lengthOfLastWord("   singleWord "))# Output: 10