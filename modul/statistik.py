from .utils import load_data

def tampilkanStatistik():
    daftarPemilih = load_data("data/pemilih.json")
    daftarCalon = load_data("data/calon.json")

    totalPemilih = len(daftarPemilih)
    sudahMemilih = sum(1 for p in daftarPemilih if p.get("sudahMemilih", False))
    belumMemilih = totalPemilih - sudahMemilih
    partisipasi = (sudahMemilih / totalPemilih) * 100 if totalPemilih > 0 else 0

    calonTerbanyak = None
    suaraTerbanyak = -1
    for c in daftarCalon:
        if c["jumlahSuara"] > suaraTerbanyak:
            calonTerbanyak = c
            suaraTerbanyak = c["jumlahSuara"]

    print("\n===== Statistik Pemilihan Umum =====")
    print(f"Total Pemilih       : {totalPemilih}")
    print(f"Sudah Memilih       : {sudahMemilih}")
    print(f"Belum Memilih       : {belumMemilih}")
    print(f"Partisipasi         : {partisipasi:.2f}%")

    if calonTerbanyak:
        print(f"\nPemenang sementara  : {calonTerbanyak['nama']} ({calonTerbanyak['id']}) dengan {calonTerbanyak['jumlahSuara']} suara")
    else:
        print("\nBelum ada suara yang masuk.")
