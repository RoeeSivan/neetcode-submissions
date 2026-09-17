class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counteText = Counter(text)
        balloon = Counter("balloon")
        res = len(text)
        for c in balloon:
            res = min(res,counteText[c] // balloon[c])
        return res