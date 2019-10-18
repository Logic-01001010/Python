T = input()
T = int(T)

for n in range(1, T+1):
    A, B = map(int, input().split())
    print("Case #",n,": ", A+B, sep = '')
