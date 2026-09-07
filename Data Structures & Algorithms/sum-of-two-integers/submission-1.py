class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b & mask:
        # Calculate the carry bits
            carry = (a & b) << 1
        # Calculate the sum without carry
            a = a ^ b
        # Move the carry to b for the next iteration
            b = carry
    # If b is greater than 0, it means we have a positive result or 
    # the carry didn't clear within 32 bits due to Python's unbounded ints.
        return (a & mask) if b > 0 else a