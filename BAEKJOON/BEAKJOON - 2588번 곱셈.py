A = input()
B = input()

A = int(A)
B = int(B)


# (3)
Three = ((B%10) * (A%10)) + ((B%10) * ((A%100)-(A%10))) + (B%10)*((A%1000)-(A%100))
print(Three)

# (4)
Four =  (((B%100-B%10) * (A%10)) + ((B%100-B%10) * ((A%100)-(A%10))) + (B%100-B%10)*((A%1000)-(A%100))) / 10
print(int(Four))

# (5)
Five =  (((B%1000-B%100) * (A%10)) + ((B%1000-B%100) * ((A%100)-(A%10))) + (B%1000-B%100)*((A%1000)-(A%100))) /100
print(int(Five))


# (6)
Six = A * B
print(Six)
