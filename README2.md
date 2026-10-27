NAMA : Erfandi Marselianus
NIM  : 2509106098
KELAS: C1





Program ini merupakan sistem pendataan hewan akuatik berbasis Python yang dirancang untuk memenuhi Posttest mata kuliah Pemrograman Berorientasi Objek (OOP). Program mensimulasikan bagaimana sebuah Balai Konservasi Perairan mengelola data hewan akuatik, kolam, dan peneliti yang bekerja di dalamnya.

# Sistem Pendataan Hewan Akuatik

Posttest Pemrograman Berorientasi Objek — Relasi UML & Inheritance.

## Fitur
- Relasi UML: Asosiasi, Agregasi, Komposisi
- Inheritance: 1 superclass, 2 subclass
- Access modifier: Protected & Private

## Struktur Class
- `HewanAkuatik` (superclass)
  - `Ikan` (subclass)
  - `Krustasea` (subclass)
- `Peneliti` → `PenelitiAkuatik` (Asosiasi)
- `Kolam` → `KolamAgregasi` (Agregasi)
- `InstansiKonservasi` ◆ `Laboratorium` (Komposisi)

## Cara Jalankan
```bash
python main.py

