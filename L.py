# Latihan logika dan komparasi 

# membuat gabungan area rentang dari angka 
# +++++3-----10++++++

inputUser = float(input("masukan angka yang bernilai\nkurang dari 3\natau \nlebih besar dari 10: "))

# +++++3----------
# Mememriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 = ", isKurangDari)

# -----------10++++++
# Memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihDari)


print("\n")
# +++++3-----10++++++
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan: ", isCorrect)

print("\n", 10*"=", "\n")# ---------------

# --------3+++++++10-------
# Kasus irisan

inputUser = float(input("masukan angka yang bernilai\nlebih dari 3\ndan \nkurang dari 10: "))

# -------3+++++++
isLebihDari = inputUser > 3
print("Lebih dari 3 =", isLebihDari)

# +++++++10----------
isKurangDari = inputUser < 10
print("Kurang dari 10 =", isKurangDari)

print("\n")

isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukan: ", isCorrect)

