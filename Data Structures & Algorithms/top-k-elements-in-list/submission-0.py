class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = {}
        for num in nums:
            if num not in arr:
                arr[num] = 0
            arr[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in arr.items():
            buckets[freq].append(num)
        
        output = []
        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                output.append(num)
                if len(output) == k:
                    return output
            

