class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        res = True
        counter = Counter()
        for word in words:
            counter += Counter(word)
        for char in counter:
            if counter[char] % len(words) != 0:
                res = False
        return res