array = [0]*9

for i in range(9):
    array[i] = int(input())

print(max(array))
print(array.index(max(array))+1)
