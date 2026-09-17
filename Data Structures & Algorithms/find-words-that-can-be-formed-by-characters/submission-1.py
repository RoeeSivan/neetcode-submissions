class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        wordict = Counter(chars) #the general dictionary for the chars
        res = 0
        for word in words:
            is_valid = True
            dic = Counter(word) # the specific dictionary for the word
            for char in dic:
                if dic[char] > wordict[char]:
                    is_valid = False
                    break
            if is_valid:
                res += len(word)
        return res
        