class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two pointers
        left = 0 
        right = len(s) - 1
        while left < right:
            # if the character is not valid, we skip it
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            # Move both pointers inward
            left += 1
            right -= 1
            
        return True
