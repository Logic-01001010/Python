Point = input()

Point = int(Point)

if Point % 4 == 0 and Point % 100 >= 1 or Point % 400 == 0:
    print("1")
else :
    print("0")
