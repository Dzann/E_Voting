from modul import pemilih, calon, voting, statistik

def main():
    while True:
        print("\n===== SISTEM E-VOTING PEMILIHAN KETUA ORGANISASI=====")
        print("1. Daftar Pemilih")
        print("2. Daftar Calon Ketua")
        print("3. Voting")
        print("4. Tampilkan Hasil")
        print("5. Tampilkan Statistik")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            pemilih.tambahPemilih()
        elif pilihan == "2":
            calon.tambahCalon()
        elif pilihan == "3":
            voting.pemungutan()
        elif pilihan == "4":
            voting.tampilkanHasil()
        elif pilihan == "5":
            statistik.tampilkanStatistik()
        elif pilihan == "6":
            print("Terima kasih Telah Menggunakan Jasa Kami!!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()