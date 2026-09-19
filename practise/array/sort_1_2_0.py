# def sort_0_1_2(nums):
#     low,mid,high=0,0,len(nums)-1
#     while mid<=high:
#         if nums[mid]==0:
#             nums[low],nums[mid]=nums[mid],nums[low]
#             low +=1
#             mid +=1
#         elif nums[mid]==1:
#             mid +=1
#         else:
#             nums[mid],nums[high]=nums[high],nums[mid]
#             high -=1

# print(sort_0_1_2(nums))
# print(nums)
# nums=[1,0,1,0,2,0,2]


# def sort_arr(nums):
#     low,mid,high=0,0,len(nums)-1
#     while mid<=high:
#         if nums[mid]==0:
#             nums[low],nums[mid]=nums[mid],nums[low]
#             low +=1
#             mid +=1
#         elif nums[mid] ==1:
#             mid +=1
#         else:
#             nums[mid],nums[high]=nums[high],nums[mid]
#             high -=1
#     return nums

# print(sort_arr(sort_arr(nums)))

nums = [7, 0, 0, 1, 7, 7, 2, 7, 7] 
# def majority_element(nums):
#     freq={}
#     for num in nums:
#         if num in freq:
#             freq[num] +=1
#         else:
#             freq[num]=1
#     # return freq

#     for key,value in freq.items():
#         if value > (len(nums)//2):
#             return key

# print(majority_element(nums))

#boyer moore voting algo
# def optimal_majority_element(nums):
#     candidate=None
#     count=0
#     for num in nums:
#         if count ==0:
#             candidate =num
#         if candidate==num:
#             count +=1
#         else: count -=1
#     return candidate

# print(optimal_majority_element(nums))

nums = [2, 3, 5, -2, 7, -4]  
def max_subarr(nums):
    n=len(nums)
    max_sum=0
    for i in range(n):
        for j in range(i,n+1):
            curr_sum=0
            for k in range(i,j):
                curr_sum +=nums[k]
            max_sum=max(max_sum,curr_sum)
    return max_sum

# print(max_subarr(nums))


# def optimal_max_subarr(nums):
#     n=len(nums)
#     max_sum=float('-inf')
#     curr_sum=0
#     for i in range(n):
#         curr_sum +=nums[i]
#         max_sum =max(max_sum,curr_sum)
#         if curr_sum <0:
#             curr_sum=0
#     return max_sum

# print(optimal_max_subarr(nums))
