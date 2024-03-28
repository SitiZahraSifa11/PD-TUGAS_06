print("\nNo.7")
# A B A B A
# B A B A B
# A B A B A
# B A B A B

susun = 'AB'
b= 4
k = 5
for i in range(b):
    for j in range(k):
        print(susun[(i+j)%2], end=" ")
    print()