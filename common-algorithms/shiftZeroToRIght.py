def shiftZerosToRight(self, nums):
    i=0
    j=0
    while i < len(nums):
        if nums[i] == 0:
            i+=1
        else:
            nums[j]=nums[i]
            i+=1
            j+=1
    while j < len(nums):
        nums[j] = 0
        j+=1
    return len(nums)