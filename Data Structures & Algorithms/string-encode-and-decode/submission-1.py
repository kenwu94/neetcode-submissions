class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        for word in strs:
            output.append(str(len(word)))
            output.append('#')
            output.append(word)
        return ''.join(output)

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        n = len(s)
        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            output.append(s[start:end])
            i = end
        return output

