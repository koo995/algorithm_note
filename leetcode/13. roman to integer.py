class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
                        "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        result = 0
        point = 0
        while point < len(s):
            c = s[point]
            if (c == "I" or c == "X" or c == "C") and point + 1 < len(s):
                n_c = s[point + 1]
                if c + n_c in symbol_value:
                    result += symbol_value[c + n_c]
                    point += 2
                    continue
            result += symbol_value[c]
            point += 1
        return result