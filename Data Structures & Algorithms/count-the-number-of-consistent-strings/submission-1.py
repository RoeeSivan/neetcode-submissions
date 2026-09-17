class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedset = set(allowed)
        consistentCount  = 0
        for word in words:
            isConsistent = True
            for char in word:
                if char not in allowedset:
                    isConsistent = False
                    break
            if isConsistent:
                consistentCount += 1
        return consistentCount
        