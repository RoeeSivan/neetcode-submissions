class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i, pattern in enumerate(words):
            for j, text in enumerate(words):
                if i != j and pattern in text:
                    res.append(pattern)
                    break
        return res
        