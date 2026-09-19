# def reverse_digits(n:int):
#     temp=n
#     rev=0
#     while n>0:
#         last_digit=n%10
#         rev =rev*10+last_digit
#         n //=10
#     if rev == temp:
#         return True
#     else:
#         return False

# print(reverse_digits(121))

# def gcd(n1,n2):
#     while n1>0 and n2>0:
#         if n1>n2:
#             n1=n1%n2 
#         else:
#             n2=n2%n1 

#     if n1==0:
#         return n2 
#     return n1
        
# print(gcd(9,12))

# def armstrong_num(n):
#     temp=n
#     result=0
#     while n>0:
#         last_digit=n%10
#         result = result + last_digit ** 3
#         n //=10

#     if result == temp:
#         return True
#     else:
#         return False


# print(armstrong_num(15))

# def all_divisor(n):
#     res=[]
#     for i in range(1,n+1):
#         if n%i==0:
#             res.append(i)
#     return res

# print(all_divisor(36))

# def checkPrime(n):
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count +=1
#     return count == 2

# print(checkPrime(232))

# def count_even_odd(n):
#     even_count=0
#     odd_count=0
#     while n > 0:
#         last_digits=n%10
#         if last_digits % 2 == 0:
#             even_count +=1
#         else:
#             odd_count +=1
#         n //=10
#     return [even_count,odd_count]

# print(count_even_odd(234567))


# def largest_digit(n):
#     largest=-1
#     while n:
#         last_digit=n%10
#         if last_digit > largest:
#             largest =last_digit
#         n //=10
#     return largest

# print(largest_digit(78323))

# def perfect_number(n:int):
#     temp=n
#     sum_value=0
#     for i in range(1,n):
#         if n%i==0:
#             sum_value +=i
#     if sum_value == temp:
#         return f"Perfect Number"
#     else:
#         return f"Not Perfect Number"
    
# print(perfect_number(6))

# def strong_number(n:int):
#     temp=n
#     total_sum=0
#     while n:
#         total=1
#         last_digit=n%10
#         for i in range(1,last_digit+1):
#             total *=i
#         total_sum +=total
#         n //=10
#     return total_sum == temp

# print(strong_number(145))


# def harshad_number(n:int):
#     temp=n
#     sum_digit =0
#     while n:
#         last_digit=n%10
#         sum_digit +=last_digit
#         n //=10
#     return temp %sum_digit==0


# print(harshad_number(18))

# def happy_number(n:int):
#     seen=set()
#     while n != 1 and n not in seen:
#         seen.add(n)
#         total_sum=0
#         while n:
#             last_digit=n%10
#             total_sum +=last_digit**2
#             n //=10
#         n=total_sum
#     if n==1:
#         return "Happy Number"
#     else:
#         return "Not Happy"


# print(happy_number(191))

#recursion
# def print_name(n:int,count:int=0):
#     if count == n:
#         return 
#     print ("Abhishek")
#     print_name(n,count+1)

# print_name(3)

# def print_number(n:int,count:int=1):
#     if count==n+1:
#         return
#     print(count)
#     print_number(n,count+1)

# print_number(5)

        
# def total_sum(n):
#     if n==1:
#         return 1
#     return n +total_sum(n-1)
    

# print(total_sum(5))


#print factorial
# def factorial(n:int):
#     if (n==1) or (n==0):
#         return 1
#     if n<0:
#         return 
#     return n*factorial(n-1)

# print(factorial(4))


#check string is palindrome or not
# def check_palindrome(i:int,s:str):
#     if i>=len(s)//2:
#         return True
#     if s[i] !=s[len(s)-i-1]:
#         return False
#     return check_palindrome(i+1,s)

# print(check_palindrome(0,"ABQDCBA"))

# def fib(n:int):
#     if n<=1:
#         return n
#     return fib(n-1) + fib(n-2)
# n=5

# def sere(n):
#     return [fib(i) for i in range(n+1)]

# print(sere(n))


# def highestfreq(arr):
#     freq={}
#     high_count=0
#     low_count=0
#     for num in arr:
#         if num in freq:
#             freq[num] +=1
#         else: 
#             freq[num] =1

#     high_count=max(freq.values())
#     low_count=min(freq.values())
#     return [high_count,low_count]
# arr=[10,5,10,15,10,5]
# print(highestfreq(arr))        

# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()

# for i in range(6):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# for i in range(1,6):
#     for j in range(i):
#         print(j+1,end=" ")
#     print()

# for i in range(1,6):
#     for j in range(i):
#         print(i,end=" ")
#     print()

#selection sort
arr=[13,46,24,52,20,9]


# def selection_sort(arr):
#     n=len(arr)
#     for i in range(n-1):
#         min_idx=i
#         for j in range(i+1,n):
#             if arr[j]<arr[min_idx]:
#                 min_idx=j
#         arr[i],arr[min_idx]=arr[min_idx],arr[i]

# selection_sort(arr)
# print(arr)


def largest_element(arr):
    largest=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>largest:
            largest=arr[i]
    return largest

# print(largest_element(arr))

# def smallest_element(arr):
#     smallest=arr[0]
#     for i in range(1,len(arr)):
#         if arr[i]<smallest:
#             smallest=arr[i]
#     return smallest

# print(smallest_element(arr))


# def second_largest(arr):
#     max_element=max(arr)
#     second_max=-1
#     for i in range(len(arr)):
#         if arr[i] < max_element and  arr[i] > second_max:
#             second_max=arr[i]
#     return second_max

# print(second_largest(arr))

# def second_smallest_element(arr):
#     smallest_ele = smallest_element(arr)
#     second_value=float('inf')

#     for i in range(len(arr)):
#         if arr[i]>smallest_ele and arr[i]<second_value:
#             second_value=arr[i]
#     return second_value

# print(second_smallest_element(arr))

# nums=[1,2,3,4,5]
# def is_sorted(arr):
#     for i in range(1,len(arr)):
#         if arr[i]<arr[i-1]:
#             return False
#     return True

# print(is_sorted(nums))

# def remove_sorted_element(arr):
#     if not arr: return 0
#     i=0
#     for j in range(1,len(arr)):
#         if arr[j] != arr[i]:
#             i +=1
#             arr[i]=arr[j]
#     return i+1

# arr=[22,22,78,78,78,90,91,91]
# k=remove_sorted_element(arr)
# for i in range(k+1):
#     print(arr[i])

# print(remove_sorted_element(arr))

# def rotate_array(arr):
#     temp=arr[0]
#     for i in range(1,len(arr)):
#         arr[i-1]=arr[i]
#     arr[-1]=temp
#     return arr
# arr=[1,2,3,4,5]

# print(rotate_array(arr))

# def rotate_array(arr):
#     temp=arr[-1]
#     for i in range(len(arr)-2,-1,-1):
#         arr[i+1]=arr[i]
#     arr[0]=temp
#     # return arr
# arr=[1,2,3,4,5,6,7]

# print(rotate_array(arr))

# def rotate_by_k(arr,k):
#     for _ in range(k):
#         rotate_array(arr)
#     return arr

# print(rotate_by_k(arr,2))


# using reversal approach 
# def reverse_arr(arr,start,end):
#     while start <=end:
#         arr[start],arr[end]=arr[end],arr[start]
#         start +=1
#         end -=1

# def reverse_k_element(arr,k:int,direction:str):
#     n=len(arr)
#     k %=n
#     if direction == "right":
#         reverse_arr(arr,0,n-1)
#         reverse_arr(arr,0,k-1)
#         reverse_arr(arr,k,n-1)
#     else:
#         reverse_arr(arr,0,k-1)
#         reverse_arr(arr,k,n-1)
#         reverse_arr(arr,0,n-1)
#     return arr

# arr=[1,2,3,4,5]
# print(reverse_k_element(arr,2,"right"))

#move zero at the end 
# def move_zero_end(arr):
#     j=0
#     for i in range(len(arr)):
#         if arr[i] !=0:
#             arr[i],arr[j]=arr[j],arr[i]
#             j +=1
#     return arr

# arr=[1,2,0,0,3,4,0,5]
# print(move_zero_end(arr))

# def linear_sear(arr,target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

# arr=[4,6,9,1,3]
# print(linear_sear(arr,1))

#missing number using xor
# def missing_number(arr):
#     n=len(arr)+1
#     xor1=0
#     xor2=0
    
#     #with all the elements from 0,n-1
#     for i in range(n-1):
#         xor2 ^=arr[i]

#     for i in range(1,n+1):
#         xor1 ^=i

#     return xor1 ^ xor2

# if __name__ == '__main__':
#     arr=[4,6,3,1,2]
#     print(missing_number(arr)) 


#maximum consetiuive count 
# def max_ones_consecutive(arr):
#     count=0
#     max_count=0
#     for num in arr:
#         if num == 0:
#             count = 0
#         else:
#             count +=1
#             max_count=max(count,max_count)
#     return max_count

# arr=[1,1,0,1,1,1]
# print(max_ones_consecutive(arr))


#number apper once in array
# def once_apper_in_array(arr):
# #trying bit mainuplation using xor
#     res=0
#     for num in arr:
#         res ^=num
    return res

    # freq={}
    # for num in arr:
    #     if num in freq:
    #         freq[num] +=1
    #     else:
    #         freq[num] =1

    # for i,val in freq.items():
    #     if val == 1:
    #         return i

# arr=[1,2,1,2,3]
# print(once_apper_in_array(arr))

#printing subarray 
for i in range(1,5):
    for j in range(0,i):
        print(i,end="")
    print()

