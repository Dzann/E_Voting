from .utils import load_data, save_data

def tambahCalon():
    idCalon = input("Masukkan ID Calon: ")
    nama = input("Masukkan Nama Calon: ")

    daftarCalon = load_data("data/calon.json")

    if any(c["id"] == idCalon for c in daftarCalon):
        print("ID calon sudah terdaftar!")
        return

    calonBaru = {
        "id": idCalon,
        "nama": nama,
        "visi": visi,
        "jumlahSuara": 0
    }

    daftarCalon.append(calonBaru)
    save_data("data/calon.json", daftarCalon)

    print("Calon berhasil ditambahkan!")
