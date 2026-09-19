def classic_maximum_subarray_sum(nums):
    curr_sum=float("-inf")
    max_sum=float("-inf")
    for num in nums:
        curr_sum =max(num,curr_sum+num)
        max_sum=max(curr_sum,max_sum)
    return max_sum

# nums = [-2,1,-3,4,-1,2,1,-5,4]
# print(classic_maximum_subarray_sum(nums))


def circular_maximum_subarray_sum(nums):
    total_sum = sum(nums)

    # Maximum subarray (Kadane)
    curr_max = max_sum = nums[0]

    # Minimum subarray (Kadane)
    curr_min = min_sum = nums[0]

    for num in nums[1:]:
        curr_max = max(num, curr_max + num)
        max_sum = max(max_sum, curr_max)

        curr_min = min(num, curr_min + num)
        min_sum = min(min_sum, curr_min)

    # All numbers are negative
    if max_sum < 0:
        return max_sum

    circular_sum = total_sum - min_sum

    return max(max_sum, circular_sum)


nums = [5,-3,5]
print(circular_maximum_subarray_sum(nums))