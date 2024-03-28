print("\nNo.3")
# 1 2 3 4 5
# 2 3 4 5
# 3 4 5
# 4 5
# 5

baris = 6
kolom = 7
for i in range(1, baris):
    for j in range(i, kolom - 1):
        print(j, end=" ")
    print()