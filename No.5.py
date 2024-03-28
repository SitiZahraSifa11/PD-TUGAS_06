print("\nNo.5")
# 1 3 5 7 9
# 2 5 8 11 14
# 3 7 11 15 19
# 4 9 14 19 24
# 5 11 17 23 29

b=2
for i in range(1,6):
    a=i

    for j in range(5):
        print(a, end=" ")
        a+=b
    b+=1
    print()