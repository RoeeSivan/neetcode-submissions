class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        current_whites = 0
        # step 1: Count white block in the very first window of size k
        for i in range(k):
            if blocks[i] == 'W':
                current_whites += 1
        # initialize the minimum recolors found so far to the first windows count
        min_recolors = current_whites
        # step 2: slide the windows across the rest of the string 
        for i in range(k,len(blocks)):
        # add the new block entering from the right
            if blocks[i] == 'W':
                current_whites += 1
        # remove the old block leaving from the left
            if blocks[i-k] == 'W':
                current_whites -= 1
        # update the minimum recolors if the current windows has fewer whites
            if current_whites < min_recolors:
                min_recolors = current_whites
        return min_recolors