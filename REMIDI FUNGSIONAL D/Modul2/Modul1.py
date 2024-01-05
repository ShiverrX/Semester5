# Inisialisasi dictionary untuk menyimpan data peserta
data_peserta = {}

# Fungsi untuk menambah peserta
def tambah_peserta(data_peserta):
    id_peserta = len(data_peserta)
    nama = input("Masukkan nama peserta: ")
    nilai = int(input("Masukkan nilai peserta: "))
    hasil_akhir = "Lolos" if nilai >= 75 else "Tidak Lolos"

    data_peserta[id_peserta] = {"Nama": nama, "Nilai": nilai, "Hasil Akhir": hasil_akhir}
    print("Data peserta berhasil ditambahkan!")

# Fungsi untuk mengedit nilai peserta
def edit_nilai(data_peserta, id_peserta, nilai_baru):
    if id_peserta in data_peserta:
        hasil_akhir_baru = "Lolos" if nilai_baru >= 75 else "Tidak Lolos"

        data_peserta[id_peserta]["Nilai"] = nilai_baru
        data_peserta[id_peserta]["Hasil Akhir"] = hasil_akhir_baru
        print("Data peserta berhasil diubah!")
    else:
        print("ID peserta tidak ditemukan.")

# Fungsi untuk peserta menampilkan nilai dan hasil akhir
def tampilkan_data_peserta(data_peserta, id_peserta):
    peserta = data_peserta.get(id_peserta)
    if peserta:
        print(f"Nama: {peserta['Nama']}")
        print(f"Nilai: {peserta['Nilai']}")
        print(f"Hasil Akhir: {peserta['Hasil Akhir']}")
    else:
        print("ID peserta tidak ditemukan.")

# Fungsi untuk mencari peserta berdasarkan nama
def cari_peserta(data_peserta, nama_peserta):
    hasil_cari = [id_peserta for id_peserta, peserta in data_peserta.items() if peserta['Nama'] == nama_peserta]
    return hasil_cari

# Program utama
while True:
    print("\nSelamat datang!")
    print("1. Admin - Tambah Peserta")
    print("2. Admin - Edit Nilai Peserta")
    print("3. Peserta - Tampilkan Nilai dan Hasil Akhir")
    print("4. Admin - Cari Peserta")
    print("5. Keluar")
    
    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

    if pilihan == '1':
        tambah_peserta(data_peserta)
    elif pilihan == '2':
        id_peserta = int(input("Masukkan ID peserta yang ingin diedit: "))
        nilai_baru = int(input("Masukkan nilai baru: "))
        edit_nilai(data_peserta, id_peserta, nilai_baru)
    elif pilihan == '3':
        id_peserta = int(input("Masukkan ID peserta Anda: "))
        tampilkan_data_peserta(data_peserta, id_peserta)
    elif pilihan == '4':
        nama_cari = input("Masukkan nama peserta yang ingin dicari: ")
        hasil_cari = cari_peserta(data_peserta, nama_cari)
        if hasil_cari:
            print(f"ID peserta yang ditemukan: {', '.join(map(str, hasil_cari))}")
        else:
            print("Nama peserta tidak ditemukan.")
    elif pilihan == '5':
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
