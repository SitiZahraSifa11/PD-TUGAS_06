print("\nNo.2")
# 1
# 2 3
# 3 4 5
# 4 5 6 7
# 5 6 7 8 9

for i in range(1,6):
    for j in range(i, i+i):
        print(j, end=" ")
    print()