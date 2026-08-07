class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxcount = 0

        for i in numset:
            if i - 1 not in numset:
                count = 1
                curr = i

                while curr + 1 in numset:
                    curr += 1
                    count += 1

                maxcount = max(maxcount, count)

        return maxcount