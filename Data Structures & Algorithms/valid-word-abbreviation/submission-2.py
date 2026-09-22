class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        jump = 0
        
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                # If we haven't started a number yet and the digit is '0', it's an invalid leading zero
                if jump == 0 and abbr[j] == '0':
                    return False
                jump = jump * 10 + int(abbr[j])
                j += 1
            else:
                if jump > 0:
                    i += jump
                    # If jumping puts us out of bounds before we can match the current character
                    if i >= len(word):
                        return False
                    jump = 0
                
                if word[i] != abbr[j]:
                    return False
                
                i += 1
                j += 1
                
        i += jump
        return i == len(word) and j == len(abbr)