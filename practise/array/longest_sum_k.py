def longestSubarraylength(nums,k):
    n=len(nums)
    max_length=0
    for i in range(n):
        for j in range(i,n):
            current_sum=0
            for p in range(i,j+1):
                current_sum +=nums[p]

            if current_sum == k:
                max_length=max(max_length,j-i+1)
    return max_length

nums = [10, 5, 2, 7, 1, 9]
k = 15 
# print(longestSubarraylength(nums,k))

def longestSubarray(nums, k):
    n = len(nums)
    maxLen = 0
    left = 0
    right = 0 
    sum = nums[0]
        
    while right < n:
            
        while left <= right and sum > k:
            sum -= nums[left]
            left += 1
            
        if sum == k:
            maxLen = max(maxLen, right - left + 1)
            
        right += 1
        if right < n:
            sum += nums[right]
        
    return maxLen


nums = [10, 5, 2, 7, 1, 9]
k = 15

# print(longestSubarray(nums,k))


#Length of the longest subarray with zero Sum
def longestSubarraylength(nums):
    n=len(nums)
    max_length=0
    for i in range(n):
        for j in range(i,n):
            current_sum=0
            for p in range(i,j+1):
                current_sum +=nums[p]

            if current_sum == 0:
                max_length=max(max_length,j-i+1)
    return max_length

nums = [9, -3, 3, -1, 6, -5]
# print(longestSubarraylength(nums))

def longestSubarray(nums):
    prefix_sum = 0
    max_len = 0
    seen = {}

    for i in range(len(nums)):
        prefix_sum += nums[i]

        if prefix_sum == 0:
            max_len = i + 1

        if prefix_sum in seen:
            max_len = max(max_len, i - seen[prefix_sum])
        else:
            seen[prefix_sum] = i

    return max_len


nums = [6, -2, 2, -8, 1, 7, 4, -10]
# print(longestSubarray(nums))

num1=[1,2,3,4,5]
num2=[2,3,4,5,6]

# def union_two_sorted_array(num1,num2):
#     seen=set()
#     for item in num1:
#         seen.add(item)

#     for item in num2:
#         seen.add(item)
#     return list(seen)

# print(union_two_sorted_array(num1,num2))

def union_two_sorted_array(num1,num2):
    i,j=0,0
    res=[]
    while i<len(num1) and j<len(num2):
        if num1[i] < num2[j]:
            res.append(num1[i])
            i +=1
        else:
            res.append(num2[j])
            j +=1
        

    while i<len(num1):
        res.append(nums[i])
        i +=1

    while j<len(num2):
        res.append(num2[j])
        j +=1

    return res


print(union_two_sorted_array(num1,num2))
