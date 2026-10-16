nums = [1,2,3,4,5,6,9]


# Usig the for loop 

# largest = nums[0]
# for num in nums:
# 	if num > largest:
# 		largest = num
# print(largest)


# Using the while loop

largest = nums[0]
i = 0

while i < len(nums):
    if nums[i] > largest:
        largest = nums[i]
    i = i+1

print(largest)