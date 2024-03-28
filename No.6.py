print("\nNo.6")  
# + + + + 5
# + + + 4 5
# + + 3 4 5
# + 2 3 4 5
# 1 2 3 4 5

b = 5
k = 6
for i in range(b, 0, -1):
    for j in range(1, k +1):
        if j < i :
            print("+", end=" ")
        else :
            print(j, end=" ")    
    print( )