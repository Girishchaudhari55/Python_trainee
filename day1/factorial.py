def find__fact(N):
    find =1
    for i in range(N,1,-1):
        fact = fact *i
    return fact
f1=find__fact(5)
f2=find__fact(2)
print(f1)
print(f2)