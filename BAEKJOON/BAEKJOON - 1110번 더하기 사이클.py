I = int(input())

global a
global b
global c
global d
global count

d = I
count = 1

while True:
        a = int((d%100 -d%10)*0.1)
 
        b = d%10

        c = int(a+b)

        d = (b*10)+(c%10)


        if d != I:
                count=count+1
        else: break

print(count)
