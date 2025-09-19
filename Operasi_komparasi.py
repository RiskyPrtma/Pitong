# Operasi komparasi
# Setiap hasil dari operasi komparasi

# >,<,>=,<=,==,is, is not

a = 4
b = 2
print("a = ", a)
print("a = ", b)
print("\n")

# Lebih besar dari >
print("===== lebih besar dari (>)")
hasil = a > 3
print(a, ">", 3, "=", hasil)
hasil = b > 3
print(b, ">", 3, "=", hasil)

hasil = b > 2 # False, karena 2 bukan lebih besar dari 2
print(b, ">", 2, "=", hasil )
hasil = b > 2.1 # True, karena 2.1 lebih besar dari 2
print(b, ">", 2.1, "=", hasil)

print("\n") # ----------- 

# Kurang dari < 
print("===== kurang dari (<)")
hasil = a < 3
print(a, "<", 3, "=", hasil)
hasil = b < 3
print(b, "<", 3, "=", hasil)
hasil = b < 2
print(b, "<", 2, "=", hasil)

print("\n") # ----------- 

# Lebih dari sama dengan >=
print("===== lebih dari sama dengan (>=)")
hasil = a >= 3
print(a, ">=", 3, "=", hasil)
hasil = b >= 3
print(b, ">=", 3, "=", hasil)
hasil = b >= 2
print(b, ">=", 2, "=", hasil)


print("\n") # ----------- 

# Kurang dari sama dengan <=
print("===== kurang dari sama dengan (<=)")
hasil = a <= 3
print(a, "<=", 3, "=", hasil)
hasil = b <= 3
print(b, "<=", 3, "=", hasil)
hasil = b <= 2
print(b, "<=", 2, "=", hasil)

print("\n") # ----------- 

# Sama dengan (==)
print("===== sama dengan (==)")
hasil = a == 4
print(a, "==", 4, "=", hasil)
hasil = b == 4
print(b, "==", 4, "=", hasil)

print("\n") # ----------- 

# Tdak sama dengan (!=)
print("===== sama dengan (!=)")
hasil = a != 4
print(a, "!=", 4, "=", hasil)
hasil = b != 4
print(b, "!=", 4, "=", hasil)


# ------------------------

# IS 
# untuk Mengecek apakah dua variabel menunjuk ke objek yang sama di memori.

# Mengecek apakah identitas dari kedua hal benar benar sama (yang sama bukan hanya nilainya, tapi benar benar hal yang sama persis)



