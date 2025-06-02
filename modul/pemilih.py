from .utils import load_data, save_data

def tambahPemilih():
    idPemilih = input("Masukkan ID Pemilih: ")
    nama = input("Masukkan Nama Pemilih: ")
    jurusan = input("Masukkan Jurusan Pemilih: ")

    daftarPemilih = load_data("data/pemilih.json")

    if any(p["id"] == idPemilih for p in daftarPemilih):
        print("ID sudah digunakan pemilih lain, gunakan ID lain!")
        return

    daftarPemilih.append({
        "id": idPemilih,
        "nama": nama,
        "jurusan": jurusan,
        "sudahMemilih": False
    })

    save_data("data/pemilih.json", daftarPemilih)

    print("Pemilih berhasil ditambahkan!")
