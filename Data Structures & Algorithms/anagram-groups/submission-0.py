class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        signatures = {}
        for word in strs:
            vec = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                vec[index] += 1
            if tuple(vec) not in signatures: 
                signatures[tuple(vec)] = []
            signatures[tuple(vec)].append(word)
        return list(signatures.values())
                

        