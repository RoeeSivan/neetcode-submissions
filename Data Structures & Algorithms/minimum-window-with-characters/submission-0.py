class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s) < len(t):
            return ""
    
    # Dictionary to keep track of all the unique characters and their counts in t
        count_t = Counter(t)
    
    # Dictionary to track characters in the current sliding window
        window = {}
    
    # 'have' tracks unique characters in the window that meet the count requirement in t
    # 'need' tracks total unique characters required from t
        have, need = 0, len(count_t)
    
    # Store result indices and the minimum window length
    # Initialized with a float representation of infinity
        res, res_len = [-1, -1], float('inf')
    
    # Left pointer for the sliding window
        l = 0
    
    # Expand the window using the right pointer
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1
        
        # If the current character is needed and its count matches what is required in t
            if char in count_t and window[char] == count_t[char]:
                have += 1
            
        # Try to contract the window from the left as long as it remains valid
            while have == need:
            # Update the result if the current window is smaller than previous minimums
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                
            # Remove the leftmost character to shrink the window
                left_char = s[l]
                window[left_char] -= 1
            
            # If removing this character breaks the valid criteria, decrement 'have'
                if left_char in count_t and window[left_char] < count_t[left_char]:
                    have -= 1
                
                l += 1 # Move left pointer forward
            
        l, r = res
        return s[l : r + 1] if res_len != float('inf') else ""