def swap(a,b):
    res=[]
    temp=a 
    a=b 
    b=temp 
    res.append(a)
    res.append(b)
    return res

def swap2(a,b):
    res=[]
    a,b=b,a
    res.append(a)
    res.append(b)
    return res

def swap3(a,b):
    res=[]
    a=a+b   #30
    b=a-b   #30-20 = 10
    a=a-b   #30-10 = 20
    res.append(a)
    res.append(b)
    return res

def count_digits(n):
    if n==0:return 1
    n=abs(n)
    count=0
    while n:
        n //=10
        count +=1
    return count

def count_freq(nums):
    freq={}
    for num in nums:
        if num in freq:
            freq[num] +=1
        else:
            freq[num]=1
    res=[]
    for key,value in freq.items():
        res.append([key,value])
    return res

def countVowelsAndConsonants(s: str):
        v_count=0
        c_count=0
        s=s.lower()
        for i in s:
            if i in "aeiou":
                v_count +=1
            else:
                c_count +=1
        return [v_count,c_count] 

def toggle_case(s):
    res=""
    for ch in s:
        if ch.isupper():
            res +=ch.lower()
        else:
            res +=ch.upper()
    return res

def longest_word(s):
    words=s.split()
    res=""
    for word in words:
        if len(word)>len(res):
            res=word
    return res



a,b=10,20
# print(swap3(a,b))
# print(count_freq([1, 2, 2, 3]))
print(longest_word("I love programming languages"))
