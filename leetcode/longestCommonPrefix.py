def longestCommonPrefix( strs) -> str:
        if not strs:
            return ""

        # Find the length of the shortest string
        max_length = min(len(s) for s in strs)

        prefix = ""
        for i in range(max_length):
            # Take the i-th character of the first string
            char = strs[0][i]

            # Check if all strings have the same character at position i
            for s in strs:
                if s[i] != char:
                    return prefix  # mismatch → return what we found so far

            # All strings matched at this character → add to prefix
            prefix += char

        return prefix
    
str1 = ["sdflower","flow","flight"]
str2 = ["dog","racecar","car"]

print(longestCommonPrefix(str1))
print(longestCommonPrefix(str2))