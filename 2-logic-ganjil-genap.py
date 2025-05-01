# Meminta input dari pengguna dan mengubahnya menjadi integer
n = int(input("Masukkan sebuah bilangan bulat positif (1-100): "))

# Mengecek apakah n ganjil atau genap
if n % 2 == 1:
    # Jika n ganjil, cetak "Weird"
    print("Weird")
else:
    # Jika n genap, cek rentang nilainya
    if 2 <= n <= 5:
        # Jika n di antara 2 sampai 5 (inklusif), cetak "Not Weird"
        print("Not Weird")
    elif 6 <= n <= 20:
        # Jika n di antara 6 sampai 20 (inklusif), cetak "Weird"
        print("Weird")
    elif n > 20:
        # Jika n lebih besar dari 20, cetak "Not Weird"
        print("Not Weird")