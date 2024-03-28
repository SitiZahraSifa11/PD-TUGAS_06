print("\nNo.4")
# 1 3 5 7 9
# 2 4 6 8 10
# 3 5 7 9 11
# 4 6 8 10 12
# 5 7 9 11 13

for i in range(1,6):
    a=i
    for j in range(1,6):
        print(a, end=" ")
        a+=2
    print()