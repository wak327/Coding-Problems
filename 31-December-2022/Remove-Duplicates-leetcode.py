def removeDuplicates(self, nums):
    for i in reversed(range(1,len(nums))):
        if nums[i] == nums[i-1]:
            nums.pop(i)
    return len(nums)