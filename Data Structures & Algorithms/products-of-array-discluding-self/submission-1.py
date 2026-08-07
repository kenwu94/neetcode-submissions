class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        out = [1] * length

        left = 1
        for i in range(length): 
            out[i] = left
            left *= nums[i]
        
        right = 1
        for i in range(length-1, -1, -1):
            out[i] *= right
            right *= nums[i]

        return out
            