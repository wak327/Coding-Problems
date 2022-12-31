def binarySearch(nums, target, min, max):
    if(nums[min]==target):
        return min
    if(nums[max]==target):
        return max
    mid = (min+max)//2
    if(mid==max or mid == min or nums[max]<target or nums[min]>target):
        return -1
    if(nums[mid]==target):
        return mid
    if(nums[mid]>target):
        return binarySearch(nums,target,min,mid)
    if(nums[mid]<target):
        return binarySearch(nums,target,mid,max)



nums = [1,2,3,4,5,6,7,8,9,10,11,15,19,20,35,70]
num = 70
print(binarySearch(nums,num,0,len(nums)-1))
if num in nums:
    print (nums.index(num))
else:
    print(-1)