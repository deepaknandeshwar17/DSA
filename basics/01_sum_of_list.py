nums = [2,4,6,8]

# using sum

# total = sum(nums)
# print(total)



#using for loop
 
# total = 0 
# for num in nums:
#     total = total + num
# print(total)



# using while loop

# total = 0
# i = 0
# while i < len(nums):
#     total = total + nums[i]
#     i = i+1
# print(total)



# using recursion

def array_sum(nums):
    if not nums:
        return 0

    return nums[0] + array_sum(nums[1:])

print(array_sum(nums))





























