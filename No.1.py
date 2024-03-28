print ("PERTEMUAN 06.FOR IN FOR")
print("\nJawaban ")
# Soal Pertemuan ke 06


print("\nNo.1")
# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25

baris = 6
kolom = 6

for i in range(1, baris):
    for j in range(1, kolom):
        print(j*i,end=" ")
    print()
