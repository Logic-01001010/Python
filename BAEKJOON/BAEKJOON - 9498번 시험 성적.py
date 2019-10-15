Point = input()

Point = int(Point)

if Point >= 90:
    print("A", end='')
    
elif Point >= 80:
    print("B", end='')
    
elif Point >= 70:
    print("C", end='')
    
elif Point >= 60:
    print("D", end='')
    
else:
    print("F", end='')
