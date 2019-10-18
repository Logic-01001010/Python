N, X = map(int, input().split())
array = list(map(int, input().split()))
for i in range(N):
        if X > array[i]:
                print(array[i]," ",end='',sep='')
