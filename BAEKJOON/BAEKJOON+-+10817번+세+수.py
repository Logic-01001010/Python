A, B, C = input().split()

A = int(A)
B = int(B)
C = int(C)

if A >= B and A <= C:
    print(A)
elif B <= A and B >= C:
    print(B)
elif C <= A and C >= B:
    print(C)
elif A <= B  and A >= C:
    print(A)
elif A <= B and B <= C:
    print(B)
elif A <= B and A <= C:
    print(C)
