class Solution:
    def isPalindrome(self, s: str) -> bool:
        #brute force solution
        cleaned_s = "".join(char.lower() for char in s if char.isalnum())
        s_reverse = "".join(reversed(cleaned_s))
        if cleaned_s == s_reverse:
            return True
        return False
        