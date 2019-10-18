i = int(input())

for n in range(i-1, -1, -1):
    print(" "*n,"*"*(i-n),sep='')
