import json
from .utils import load_data, save_data

def pemungutan():
    idPemilih = input("Masukkan ID pemilih: ")

    daftarPemilih = load_data("data/pemilih.json")
    daftarCalon = load_data("data/calon.json")

    for p in daftarPemilih:
        if p["id"] == idPemilih:
            if p.get("sudahMemilih", False):
                print("Anda sudah memilih sebelumnya!")
                return
            else:
                print("\nDaftar Calon:")
                for i, c in enumerate(daftarCalon):
                    print(f"{i + 1}. {c['nama']} (ID: {c['id']})")
                try:
                    pilihan = int(input("Pilih Nomor Calon: ")) - 1
                    if 0 <= pilihan < len(daftarCalon):
                        daftarCalon[pilihan]["jumlahSuara"] += 1
                        p["sudahMemilih"] = True

                        save_data("data/pemilih.json", daftarPemilih)
                        save_data("data/calon.json", daftarCalon)

                        print("Voting berhasil, terima kasih telah menggunakan hak suara Anda!")
                        return
                    else:
                        print("Pilihan tidak valid!")
                        return
                except ValueError:
                    print("Masukan harus berupa angka!")
                    return

    print("ID pemilih tidak ditemukan.")

def tampilkanHasil():
    daftarCalon = load_data("data/calon.json")

    if not daftarCalon:
        print("Tidak ada data calon.")
        return

    print("\n=== Hasil Sementara Pemilihan ===")
    for c in daftarCalon:
        print(f"Nama: {c['nama']}, ID: {c['id']}, Jumlah Suara: {c['jumlahSuara']}")
