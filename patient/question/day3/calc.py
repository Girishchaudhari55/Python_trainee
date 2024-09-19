def find_diff(first:int=1,second:int=0):
    return first - second

print(find_diff(20,10))
print(find_diff(second=10,first=20))
print(find_diff(second=10))
print(find_diff())

def change_name(names,index,name):
    names[index]=name
names =['rahul','modi']
print(names)
change_name(names,1,'modiji')
print(names)

print(sum([10,20,30]))
def find_sum(first, second,*other):
    s = first+second
    if(len(other)>0):
        for num in other:
          s += num
    return s
print(find_sum(10,20))
print(find_sum(10,20,30))
print(find_sum(10,20,30,40,50))

print(find_sum(first=10,second=20))
print(find_sum(first=10,second=20,third=50))

#factorail using recursion
def fact(N):
    if N <= 1:
        return 1  
    return N * fact(N - 1)

print(fact(5))  # Output: 120
print(fact(4))  # Output: 24


#to check the number is prime or not
import math
def is_prime(N):
    N_sqrt = int(math.sqrt(N))
    for I in range(2, N_sqrt + 1):
        if N%I==0:
            return False
        return False

    return True

# Example usage
print(is_prime(7))  # Output: True
print(is_prime(10))  # Output: False
print(is_prime(61))