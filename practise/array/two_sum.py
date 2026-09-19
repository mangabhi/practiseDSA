# def two_sum(nums,target):
#     for i in range(0,len(nums)-1):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j] == target:
#                 return "YES"
#     return "No"

nums=[2,6,5,8,11]
# print(two_sum(nums,17))

def optimal_two_sum(nums,target):
    seen={}
    for i in range(len(nums)):
        comp=target-nums[i]
        if comp in seen:
            return [seen[comp],i]
        seen[nums[i]]=i
    return []

# print(optimal_two_sum(nums,11))

#prefix and suffix
# def product_except_self(nums):
#     n=len(nums)
#     prefix=1
#     suffix=1
#     res=[1]*n
#     for i in range(n):
#         res[i]=prefix
#         prefix *=nums[i]

#     for i in range(n-1,-1,-1):
#         res[i] *=suffix
#         suffix *=nums[i]

#     return res

# nums=[1,2,3,4]
# print(product_except_self(nums))        



#flatten array
# arr = [[1, 2], [3, 4], [5, 6 ,[1,4,6]]]
# def flatten_array(arr):
#     flat=[]
#     for item in arr:
#         if isinstance(item,list):
#             for i in flatten_array(item):
#                 flat.append(i)
#         else:
#             flat.append(item)
#     return flat

# print(flatten_array(arr))


