#Two Sum


# def two_sum(arr,target):
#     n=len(arr)
#     for i in range(n):
#         for j in range(i):
#             if target == arr[i] +arr[j]:
#                 return [j,i]
#     return -1

# def two_sum_optimize(arr,target):
#     seen={}
#     for i in range(len(arr)):
#         complement=target-arr[i]
#         if complement in seen:
#             return [seen[complement],i]
#         seen[arr[i]]=i
#     return -1

# arr=[4,1,5,9,3]
# target=10
# print(two_sum_optimize(arr,target))



#contains duplicate
# def check_duplicate(nums):
#     n=len(nums)
#     for i in range(n):
#         for j in range(i):
#             if nums[i]==nums[j]:
#                 return True
#     return False

# nums = [1, 2, 3]
# # print(check_duplicate(nums))

# def check_duplicate_optimize(nums):
#     seen=set()
#     for num in nums:
#         if num in seen:
#             return True
#         seen.add(num)
#     return False
    

# print(check_duplicate_optimize(nums))
# s = "anagram"
# t = "nagaram"

# def anagram(s,t):
#     if len(s) !=len(t):
#         return False
#     s_sorted=sorted(s)
#     t_sorted=sorted(t)
#     i=0
#     while i<len(s):
#         if s_sorted[i] != t_sorted[i]:
#             return False
#         i +=1
#     return True

# # print(anagram(s,t))


# def anagram_optimise(s,t):
#     freq={}
#     for num in s:
#         freq[num]= freq.get(num,0)+1

#     for num in t:
#         if num not in freq:
#             return False

#         freq[num] -=1

#         if freq[num] <0:
#             return False

#     return True
        

# print(anagram_optimise(s,t))
# from collections import defaultdict
# def group_anagram(strs):
#     result=defaultdict(list)
#     for num in strs:
#         sorted_key="".join(sorted(num))
#         print(sorted_key)
#         result[sorted_key].append(num)
#         # print(result[sorted_key].append(num))

#     # return list(result.values())


# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(group_anagram(strs))

# def k_most_frequenet(nums,k):
#     freq={}
#     for num in nums:
#         if num in freq:
#             freq[num] +=1
#         else:
#             freq[num]=1
#     res=[]
#     sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
#     for num, count in sorted_freq:
#         res.append(num)
#     return res[:k]

# nums = [4, 4, 5, 5, 5, 6]
# k = 1
# print(k_most_frequenet(nums,k))

# def consecutive_sequence(nums):
#     nums.sort()
#     max_count=1
#     curr_count=1
#     for i in range(1,len(nums)):
#         if nums[i] == nums[i-1]:
#             continue
#         elif nums[i]==nums[i-1] +1:
#             curr_count +=1
#         else:
#             max_count=max(max_count,curr_count)
#             curr_count=1
#     return max(curr_count,max_count) 

# nums = [100, 4, 200, 1, 3, 2]
# print(consecutive_sequence(nums))

# def majority_element(nums):
#     count =0
#     candidate=None
#     for num in nums:
#         if count ==0:
#             candidate=num
#         if num == candidate:
#             count +=1
#         else:
#             count -=1
#     return candidate

# nums = [2, 2, 1, 1, 1, 2, 2]
# print(majority_element(nums))

# def prefix_sum(nums):
#     prefix=[0]*len(nums)
#     prefix[0]=nums[0]
#     for i in range(1,len(nums)):
#         prefix[i] = prefix[i-1] + nums[i] 
#     return prefix

# nums=[1,2,3,4]
# print(prefix_sum(nums))

# def prefix_sum_optimal(nums):
#     for i in range(1,len(nums)):
#         nums[i] += nums[i-1]
#     return nums
# nums=[1,2,3,4]
# print(prefix_sum_optimal(nums))

# def sum_range(nums,left,right):
#     prefix=[0]*len(nums)
#     prefix[0]=nums[0]
#     for i in range(1,len(nums)):
#         prefix[i]=prefix[i-1]+nums[i]

#     if left ==0:
#         return prefix[right]
#     return prefix[right]-prefix[left-1]

# def range_query(nums,left:int,right:int):
#     total_sum=0
#     sliced_arr =nums[left:right+1]
#     for num in sliced_arr:
#         total_sum +=num
#     return total_sum


# nums=[-2,0,3,-5,2,-1]
# print(range_query(nums,2,5))

# def range_query(nums,left:int,right:int):
#     total_sum=0
#     for i in range(left,right+1):
#         total_sum +=nums[i]
#     return total_sum


# nums=[-2,0,3,-5,2,-1]
# print(range_query(nums,2,5))

# def k_sum(nums,k):
#     count=0
#     for i in range(len(nums)):
#         curr_sum=0
#         for j in range(i,len(nums)):
#             curr_sum +=nums[j]
#             if k==curr_sum:
#                 count +=1
#     return count

# nums=[1,-1,0]
# k=0
# # print(k_sum(nums,k))


# def k_sum_optimal(nums,k):
#     count=0
#     prefix_sum=0
#     freq={0:1}
#     for num in nums:
#         prefix_sum +=num
#         if prefix_sum -k in freq:
#             count +=freq[prefix_sum-k]
#         freq[prefix_sum]=freq.get(prefix_sum,0)+1
#     return count

# print(k_sum_optimal(nums,k))

# def continous_sum_subarray(nums,k):
#     for i in range(len(nums)):
#         curr_sum=0
#         for j in range(i,len(nums)):
#             curr_sum +=nums[j]
#             if curr_sum%k==0 and j-i+1>=2:
#                 return True
#         return False

# nums = [23, 2, 6, 4, 7]
# k = 8
# print(continous_sum_subarray(nums,k))

# def continuous_sum_subarray(nums, k):
#     remainder_index = {0: -1}
#     prefix_sum = 0

#     for i, num in enumerate(nums):
#         prefix_sum += num
#         remainder = prefix_sum % k

#         if remainder in remainder_index:
#             if i - remainder_index[remainder] >= 2:
#                 return True
#         else:
#             remainder_index[remainder] = i

#     return False
# print(continuous_sum_subarray(nums,k))

# def array_except_self(nums):
#     prefix=1
#     res=[1]*len(nums)
#     for i in range(len(nums)):
#         res[i]=prefix
#         prefix *=nums[i]

#     suffix=1
#     for i in range(len(nums)-1,-1,-1):
#         res[i] *=suffix
#         suffix *=nums[i]

#     return res

# def array_except_self(nums):
#     n=len(nums)
#     left=[1]*n
#     right=[1]*n
#     res=[1]*n
#     for i in range(1,n):
#         left[i]=left[i-1]*nums[i-1]
#     for i in range(n-2,-1,-1):
#         right[i]=right[i+1]*nums[i+1]
#     for i in range(n):
#         res[i]=left[i]*right[i]
#     return res

# nums=[1,2,3,4]
# print(array_except_self(nums))

# def two_sum_sorted(nums,target):
#     low,high=0,len(nums)-1
#     while low<high:
#         if nums[low]+nums[high] == target:
#             return [low,high]
#         elif nums[low]<nums[high]:
#             high -=1
#         else:
#             low +=1
#     return -1

# nums=[2,3,4]
# target=6
# print(two_sum_sorted(nums,target))


# def valid_palindrome(s):
#     low,high=0,len(s)-1
#     while low<high:
#         while low<high and not s[low].isalnum():
#             low +=1
#         while low<high and not s[high].isalnum():
#             high -=1
#         if s[low].lower() !=s[high].lower():
#             return False
#         low +=1
#         high -=1
#     return True

# print(valid_palindrome("amanaplanacanalpanama"))

# def remove_duplciated_sorted(nums):
#     res=[nums[0]]
#     for i in range(1,len(nums)):
#         if nums[i]>nums[i-1]:
#             res.append(nums[i])
#     return res

# nums=[0,0,1,1,2,2,2,3,3,4]
# print(remove_duplciated_sorted(nums))


# def move_zero(nums):
#     j=0
#     for i in range(len(nums)):
#         if nums[i] !=0:
#             #swap
#             nums[i],nums[j]=nums[j],nums[i]
#             j +=1
#     return nums

# nums=[1,0,0,2,3,0,5,7,0]
# print(move_zero(nums))


#sort color
# def sort_color(nums):
#     low,mid,high=0,0,len(nums)-1
#     while mid<=high:
#         if nums[low]==0:
#             nums[low],nums[mid]=nums[mid],nums[low]
#             low +=1
#             mid +=1
#         elif nums[mid] ==1:
#             mid +=1
#         else:
#             nums[mid],nums[high]=nums[high],nums[mid]
#             high -=1
#     return nums

# nums=[2,0,2,1,1,0]
# print(sort_color(nums))

#containing water
# def containing_most_water(nums):
#     max_water=0
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             width=j-i
#             area=min(nums[i],nums[j])*width
#             max_water=max(max_water,area)
#     return max_water

# nums=[2,3,4,5,18,17,6]
# print(containing_most_water(nums))

# def containing_water_most_optimise(height):
#     low,high=0,len(height)-1
#     max_water=0
#     while low<high:
#         area=min(height[low],height[high])*(high-low)
#         max_water=max(max_water,area)

#         if height[low]<height[high]:
#             low +=1
#         else:
#             high -=1
#     return max_water

# nums = [2, 3, 4, 5, 18, 17, 6]
# print(containing_water_most_optimise(nums))

#trapping rain water
# def trapping_rain_water(nums):
#     max_unit=0
#     n=len(nums)
#     for i in range(n):
#         left_max=0
#         right_max=0
#         for left in range(i+1):
#             left_max=max(left_max,nums[left])
#         for right in range(i,n):
#             right_max=max(right_max,nums[right])
#         max_unit +=min(left_max,right_max)-nums[i]
#     return max_unit 
# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# print(trapping_rain_water(height))  # 6

# def trapping_rain_water(height):
#     left, right = 0, len(height) - 1
#     left_max, right_max = 0, 0
#     total_water = 0

#     while left < right:
#         if height[left] <= height[right]:
#             if height[left] >= left_max:
#                 left_max = height[left]
#             else:
#                 total_water += left_max - height[left]
#             left += 1
#         else:
#             if height[right] >= right_max:
#                 right_max = height[right]
#             else:
#                 total_water += right_max - height[right]
#             right -= 1

#     return total_water


# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# print(trapping_rain_water(height))  # 6

#sliding window
#maximum average subarray
# def max_avg_subarray(nums,k):
#     n=len(nums)
#     max_sum=0
#     for i in range(0,n-k+1):
#         curr_sum=0
#         for j in range(i,k+i):
#             curr_sum +=nums[j]
#         max_sum =max(max_sum,curr_sum/k)
#     return max_sum



# nums = [1,12,-5,-6,50,3]
# k = 4
# print(max_avg_subarray(nums,k))

# def max_avg_subarray_optimize(nums,k):
#     window_sum=sum(nums[:k])
#     max_sum=window_sum
#     for i in range(k,len(nums)):
#         window_sum =window_sum + nums[i]-nums[i-k]
#         max_sum=max(max_sum,window_sum)
#     return max_sum/k
# nums = [1,12,-5,-6,50,3]
# k = 4

# print(max_avg_subarray_optimize(nums,k))


#Maximum Sum Subarray of Size K
# def max_sum_subarray(nums,k):
#     max_sum=0
#     for i in range(len(nums)-k+1):
#         curr_sum=0
#         for j in range(i,i+k):
#             curr_sum +=nums[j]
#         max_sum =max(max_sum,curr_sum)
#     return max_sum

# nums = [2, 1, 5, 1, 3, 2]
# k = 3
# print(max_sum_subarray(nums,k))

# def optimise_max_sum_array(nums,k):
#     window_sum=sum(nums[:k])
#     max_sum=window_sum
#     for i in range(k,len(nums)):
#         window_sum +=nums[i]-nums[i-k]
#         max_sum=max(max_sum,window_sum)
#     return max_sum

# nums = [2, 1, 5, 1, 3, 2]
# k = 3
# print(optimise_max_sum_array(nums,k))


#Sliding Window Maximum
# def maximum_element(nums,k):
#     res=[]
#     max_element=float('-inf')
#     for i in range(len(nums)-k+1):
#         curr_max=float('-inf')
#         for j in range(i,i+k):
#             curr_max=max(nums[j],curr_max)
#         max_element=max(max_element,curr_max)
#         res.append(max_element)
#     return res

# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
# print(maximum_element(nums,k))

# def optimize_max_element(nums,k):
#     window_max=max(nums[:k])
#     res=[]
#     for i in range(k,len(nums)):
#         window_max =max(nums[i-k+1:i+1])
#         res.append(window_max)
#     return res

# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
# print(optimize_max_element(nums,k))

#Longest Substring Without Repeating Characters
# def longest_substring_length(s):
#     max_len=0
#     for i in range(len(s)):
#         seen=set()
#         for j in range(i,len(s)):
#             if s[j]in seen:
#                 break
#             seen.add(s[j])
#             max_len=max(max_len,j-i+1)
#     return max_len
# s="abcabcbb"
# print(longest_substring_length(s))


# def longest_substring_length_optimise(s):
#     seen=set()
#     left=0
#     max_len=0
#     for right in range(len(s)):
#         while s[right] in seen:
#             seen.remove(s[left])
#             left +=1
#         seen.add(s[right])
#         max_len=max(max_len,right-left+1)
#     return max_len
# s="abcabcbb"
# print(longest_substring_length_optimise(s))


#Binary search
# def binary_search(nums,target):
#     left,right=0,len(nums)-1
#     while left<=right:
#         mid=(right+left)//2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] <target:
#             left +=1
#         else:
#             right -=1
#     return -1

# nums = [-1,0,3,5,9,12]
# target = 9
# print(binary_search(nums,target))



#Search Insert Position
# def binary_search(nums,target):
#     left,right=0,len(nums)-1
#     while left<=right:
#         mid=(right+left)//2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] <target:
#             left +=1
#         else:
#             right -=1
#     return left

# nums = [1, 3, 5, 6]
# target = 2
# print(binary_search(nums,target))

