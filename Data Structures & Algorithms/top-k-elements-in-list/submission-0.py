class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
        
                my_dict[num] = 1
        sorted_keys = sorted(my_dict.keys(), key=lambda x: my_dict[x], reverse=True)
        
        # Return the first k elements
        return sorted_keys[:k]   