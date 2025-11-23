class Solution:
    def romanToInt(s: str) -> int:
        result = 0
        symbol_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        for i in range(len(s)):
            value = symbol_dict[s[i]]
            if i + 1 < len(s) and symbol_dict[s[i + 1]] > value:
                result -= value
            else:
                result += value

        return result

if __name__ =='__main__':
    print(Solution.romanToInt("IV"))
    print(Solution.romanToInt("MMXXIV"))
