# # nums=[1, 2, 0, 4, 3, 0, 5, 0]
# def move_zero(nums):
#     j=0
#     for i in range(len(nums)):
#         if nums[i]!=0:
#             nums[i],nums[j]=nums[j],nums[i]
#             j +=1
#     return nums

# def triplet_sum(arr,target):
#     arr.sort()
#     low,mid,high=0,1,2
#     while mid<high:
#         s=arr[low]+arr[mid]+arr[high]
#         if s == target:
#             return "true"
#         elif s<target:
#             high +=1
#             low +=1
#             mid +=1
#         else:
#             return "false"
        


# arr = [1, 4, 45, 6, 10, 8]
# target = 13
# print(triplet_sum(arr,target))


#kadane problem
# def max_subarray_sum(nums):
#     curr_sum=0
#     max_sum=float("-inf")
#     for num in nums:
#         curr_sum =max(num,curr_sum + num)
#         max_sum=max(max_sum,curr_sum)
#     return max_sum

# nums = [2, 3, 5, -2, 7, -4] 
# print(max_subarray_sum(nums))

# def max_subarray_sum_brute(nums):
#     max_sum=float("-inf")
#     for i in range(len(nums)):
#         for j in range(i,len(nums)):
#             curr_sum=0
#             for k in range(i,j+1):
#                 curr_sum +=nums[k]
#             max_sum=max(max_sum,curr_sum)
#     return max_sum

# print(max_subarray_sum_brute(nums))

def stock_buy_sell(prices):
    min_price=float('inf')
    max_profit=0
    for price in prices:
        min_price=min(min_price,price)
        profit=price-min_price
        max_profit=max(max_profit,profit)
    return max_profit

prices = [7,1,5,3,6,4]
# print(stock_buy_sell(prices)) 

# def stock_buy_sell_brute(prices):
#     max_profit=0
#     for i in range(len(prices)):
#         for j in range(i+1,len(prices)):
#             profit = prices[j]-prices[i]
#             max_profit=max(max_profit,profit)
#     return max_profit

# print(stock_buy_sell_brute(prices)) 

# def arrange_element_sign(arr):
#     neg=[]
#     pos=[]
#     i=0
#     for num in arr:
#         if num<0:
#             neg.append(num)
#         else:
#             pos.append(num)

#     res=[0]*len(arr)
#     for i in range(len(neg)):
#         res[2*i+1]=neg[i]

#     for i in range(len(pos)):
#         res[2*i]=pos[i]

#     return res

# arr=[1,2,3,-1,-2,-3]
# print(arrange_element_sign(arr)) 

# def arrange_element_sign(arr):
#     res=[0]*len(arr)
#     pos=0
#     neg=1
#     for i in range(len(arr)):
#         if arr[i]<0:
#             res[neg]=arr[i]
#             neg +=2
#         else:
#             res[pos]=arr[i]
#             pos +=2
#     return res

# arr=[1,2,3,-1,-2,-3]
# print(arrange_element_sign(arr))

# def leader_array(arr):
#     res=[]
#     max_right = arr[-1]
#     res.append(max_right)
#     for i in range(len(arr)-2,-1,-1):
#         if arr[i]>=max_right:
#             max_right=arr[i]
#             res.append(arr[i])
#     return res[::-1]

# arr=[4,7,1,0]
# print(leader_array(arr))
# def longest_sequence(arr):
#     arr.sort()
#     min_value=min(arr)
#     count=0
#     # count1=1
#     for i in range(min_value,len(arr)):
#         if arr[i] == i:
#             count +=1
#     return count

# nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]  
# print(longest_sequence(nums))

# def subarray_k(arr,k):
#     count=0
#     curr_sum=0
#     for num in arr:
#         count +=1
#         curr_sum=curr_sum+num
#     if curr_sum == k:
#         return count
#     return count

# arr=[3,1,2,4]
# k=6
# print(subarray_k(arr,k))

def lower_bound(arr,x):
    low=0
    while low<len(arr):
        if arr[low]>=x:
            return low
        else:
            low +=1
    return low
arr=[1,2,2,3]
x=2
print(lower_bound(arr,x))