class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # array or map to store the last seen index of a b c , initialized to -1
        lastSeen = {'a':-1,'b':-1,'c':-1}
        totalCount = 0
        n = len(s)
        for i in range(n):
            currentChar = s[i]
            lastSeen[currentChar] = i
            # check if all three characters have appeared at least once
            if lastSeen['a'] != -1 and lastSeen['b'] != -1 and lastSeen['c'] != -1:
                #the number of valid substrings ending at index i
                minLastSeen = min(lastSeen['a'],lastSeen['b'],lastSeen['c'])
                totalCount = totalCount + (minLastSeen +1)
        return totalCount
                
        
