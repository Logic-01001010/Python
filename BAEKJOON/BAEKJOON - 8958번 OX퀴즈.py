n = int(input())

for i in range(n):
    array = input()
    Sum = 0
    Add = 0
    
    for j in range(len(array)):
        if array[j] == 'O':
            Add = Add + 1
            Sum = Sum + Add
        else:
            Add = 0
    print(Sum)
            
