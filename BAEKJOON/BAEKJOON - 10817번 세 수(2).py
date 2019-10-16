A, B, C = input().split()

A = int(A)
B = int(B)
C = int(C)

Max = max(A, B, C)
Min = min(A, B, C)

print((A+B+C)-(Max+Min))
