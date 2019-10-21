C = int(input())

for i in range(C):
    array = list(map(int, input().split()))
    GreatStudents = 0

    for j in range(array[0]):
        if ((sum(array)-array[0]) / array[0]) < array[j+1]:
            
            GreatStudents = GreatStudents + 1
            
    print('%0.3f' % round(100 * GreatStudents / array[0], 3),"%",sep='')      
