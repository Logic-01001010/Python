N = int(input())

array = list(map(int,input().split()))
Min = array[0]
Max = array[0]

for i in range(N):
    if array[i] >= Max:
        Max = array[i]
    if array[i] <= Min:
        Min = array[i]

print(Min, Max)
    
