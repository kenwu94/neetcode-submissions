class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            k = (l + r) // 2

            if nums[k] == target:
                return k
            
            if nums[l] <= nums[k]:
                if target < nums[l] or target > nums[k]:
                    l = k + 1
                else:
                    r = k - 1
                    
            else:
                if target > nums[r] or target < nums[k]:
                    r = k - 1
                else:
                    l = k + 1
        return -1
           
                