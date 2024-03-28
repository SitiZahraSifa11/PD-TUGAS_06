print("\nNo.8")
# S O S O S
# O S O S
# S O S
# O S
# S

susun = 'SO'
b= 5
k = 5
for i in range(b):
    for j in range(k-i):
      print(susun[(i+j)%2], end=" ")
    print()