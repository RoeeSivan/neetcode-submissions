class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers) 
        # Step 1: Customers satisfied without using the technique
        baseline = 0
        for i in range(n):
            if grumpy[i] == 0:
                baseline += customers[i]
        # Step 2: Sliding window to find max additional satisfied customers
        extra = 0 
        curr = 0 
        for i in range(n):
            if grumpy[i] == 1:
                curr += customers[i]
            if i >= minutes:
                if grumpy[i - minutes] == 1:
                    curr -= customers[i - minutes]
            extra = max(extra, curr)
            
        return baseline + extra