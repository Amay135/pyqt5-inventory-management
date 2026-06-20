# Simple Inventory Management System (PyQt5)

Aplikasi desktop sederhana untuk manajemen data barang (inventaris) yang dibuat menggunakan **Python** dan **PyQt5**. Proyek ini dilengkapi dengan fitur autentikasi sederhana (Login & Registrasi Pengguna) serta fitur *Create* dan *Delete* data barang ke dalam tabel berbasis GUI.

## Fitur Utama

* **Sistem Registrasi & Login:** Autentikasi akun pengguna (sementara disimpan di memori/in-memory database).
* **Manajemen Barang:** Menambahkan data nama barang, jumlah, dan harga ke dalam tabel (`QTableWidget`).
* **Hapus Data:** Menghapus baris data barang yang dipilih dari tabel.
* **Modular UI:** Desain antarmuka dibuat menggunakan Qt Designer (`.ui`) dan dikonversi ke kode Python (`.py`).

## 🛠️ Prasyarat (Prerequisites)

Sebelum menjalankan aplikasi, pastikan Anda sudah menginstal Python (versi 3.x) dan pustaka PyQt5 di komputer Anda.

```bash
pip install PyQt5
```

## Struktur File

├── daftar.ui          # Desain UI untuk halaman registrasi (Qt Designer)
├── daftar.py          # Hasil konversi daftar.ui ke Python
├── login.ui           # Desain UI untuk halaman login (Qt Designer)
├── login.py           # Hasil konversi login.ui ke Python
├── mainlayout.ui      # Desain UI untuk halaman utama/tabel (Qt Designer)
├── mainlayout.py      # Hasil konversi mainlayout.ui ke Python
└── main.py            # Alur logika utama aplikasi (Main Entry Point)

## Catatan Pengembangan

Aplikasi ini saat ini masih menggunakan penyimpanan berbasis memori (users_db), sehingga data akun dan barang akan ter-reset ketika aplikasi ditutup. Proyek ini sangat cocok dijadikan fondasi dasar bagi pemula yang ingin belajar PyQt5 sebelum dikembangkan lebih lanjut dengan integrasi database permanen seperti SQLite atau MySQL.
