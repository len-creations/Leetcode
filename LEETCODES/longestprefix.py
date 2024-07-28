from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       #  the initialize prefix
        prefix = strs[0]
        
        # Iterating through the remaining strings
        for string in strs[1:]:
            # Reduce the prefix until it matches the start of the current string
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                # If the prefix becomes empty, return an empty string
                if not prefix:
                    return ""
        
        return prefix

# Instantiate the Solution class
sol = Solution()

# Call the method on the instance
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "