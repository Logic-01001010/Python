N = int(input())
arr = list(map(int,input().split()))
a =0
for i in range(N):
    a += arr[i]/max(arr)*100

print(a/N)
