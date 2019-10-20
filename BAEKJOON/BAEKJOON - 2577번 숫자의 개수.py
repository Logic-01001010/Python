A = input()

B = input()

C = input()

Result = int(A) * int(B) * int(C)

Result = str(Result)

for i in range(0, 10):
    print(Result.count(str(i)))
