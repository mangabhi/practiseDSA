def swap(a,b):
    a=a^b
    b=a^b
    a=a^b
    print(a,b)

# swap(10,20)

def convert_to_binary(n:int):
    res=""
    while n !=0:
        if n%2==1:
            res ='1' +res
        else:
            res ='0' +res
        n //=2
    return res


# print(convert_to_binary(13))

def check_odd(n:int):
    return "true" if n%2==1 else "false"

# print(check_odd(100))

def count_bits():
    count=0
    res=convert_to_binary(5)
    for char in res:
        if char == '1':
            count +=1
    return count

# print(count_bits())

def check_power(n):
    if n<=0:
        return "false"
    temp=n
    count=0
    while n!=0:
        if n%2==0:
            count +=1
        n //=2
    return "true" if temp == 2**count else "false"

# print(check_power(16))

def i_th_bit(n,k):
    res=convert_to_binary(n)
    return res[-(k+1)] == '1'

print(i_th_bit(5,0))

def without_operator():
    a,b=7,3
    count=0
    while a>=b:
        a -=b
        count +=1
    return count

print(without_operator())




