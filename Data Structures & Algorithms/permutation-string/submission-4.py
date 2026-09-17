class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        k = len(s1)

        counters1 = Counter(s1)
        counters2 = Counter(s2[:k])
        if counters1 == counters2:
            return True
        
        for i in range(k,len(s2)):
            counters2[s2[i]] += 1
            counters2[s2[i-k]] -= 1
            if counters1 == counters2:
                return True
        return False


        
        