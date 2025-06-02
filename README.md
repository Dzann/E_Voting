# 🗳️ Simulasi E-Voting Pemilihan Ketua Organisasi Mahasiswa

Sistem ini merupakan simulasi pemilu elektronik (e-voting) berbasis Python yang digunakan untuk memilih ketua organisasi mahasiswa. Sistem ini mencakup pencatatan data pemilih dan calon ketua, proses pemungutan suara, serta statistik hasil pemilu.

---

## 📌 Fitur Utama

- 📋 **Manajemen Pemilih**  
  Tambah pemilih baru dengan ID unik dan data jurusan.

- 🧑‍💼 **Manajemen Calon Ketua**  
  Tambah calon ketua dengan data visi dan perhitungan suara otomatis.

- ✅ **Pemungutan Suara (Voting)**  
  Validasi ID pemilih dan calon. Pemilih hanya dapat memilih satu kali.

- 📊 **Hasil Sementara dan Statistik**  
  Menampilkan hasil perolehan suara dan statistik partisipasi pemilu.

---

## 🗂️ Struktur Proyek

```plaintext
evoting/
├── main.py # Menu utama CLI
├── modul/
│   ├── __init__.py
│   ├── utils.py # Fungsi bantu: load_data, save_data
│   ├── pemilih.py # Tambah pemilih
│   ├── calon.py # Tambah calon ketua
│   ├── voting.py # Proses pemungutan suara dan hasil
│   └── statistik.py # Statistik partisipasi dan perolehan suara
└── data/
    ├── pemilih.json # Data pemilih (tersimpan sebagai list of dict)
    └── calon.json # Data calon ketua

