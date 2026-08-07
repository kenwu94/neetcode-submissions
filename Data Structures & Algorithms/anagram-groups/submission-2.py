class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for i in strs:
            cur = [0] * 26
            for j in i:
                cur[ord(j) - ord('a')] += 1
            
            res[tuple(cur)].append(i)
        
        return list(res.values())

        