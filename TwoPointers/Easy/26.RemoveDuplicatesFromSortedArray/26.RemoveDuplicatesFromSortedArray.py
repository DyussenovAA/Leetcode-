class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        uniqe_ptr = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[uniqe_ptr]:
                uniqe_ptr += 1
                nums[uniqe_ptr] = nums[i]

        return uniqe_ptr + 1
