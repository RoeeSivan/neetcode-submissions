class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            my_map[key].append(word)
        return list(my_map.values())
