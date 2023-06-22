class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.res: List[str] = []
        if digits=="":
            return []
        mapping: Dict[str, str] =  {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backtrack(combination, next_digits, mapping):
            if not next_digits:
                self.res.append(combination)
                return
            for letter in mapping[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:], mapping)
        backtrack("", digits, mapping)
        return self.res
