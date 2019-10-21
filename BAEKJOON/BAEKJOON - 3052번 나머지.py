li = [999]*10
n = 0
for i in range(10):
    a = int(input())
    if li.count(a%42) == 0:
        li[i] = a%42
        n=n+1      
print(n)
