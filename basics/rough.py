nums = [1,2,3,4,15,16]

largest = nums[0]

for i in range(1,len(nums)):
    if nums[i] > largest:co
        largest = nums[i]

print(largest)