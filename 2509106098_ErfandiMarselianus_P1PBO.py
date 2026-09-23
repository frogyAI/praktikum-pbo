from datetime import datetime


class HewanAkuatik:
    nama_instansi = "Balai Konservasi Perairan Mulawarman"
    total_hewan_terdaftar = 0
    suhu_ideal_default = 27.0

    def __init__(self, nama_spesies, habitat, suhu_ideal, jumlah):
        self.nama_spesies = nama_spesies
        self.habitat = habitat
        self.suhu_ideal = suhu_ideal
        self.__jumlah = jumlah
        self.__total_diamati = 0

        HewanAkuatik.total_hewan_terdaftar += 1

    @property
    def jumlah(self):
        return self.__jumlah

    @jumlah.setter
    def jumlah(self, nilai_baru):
        if not isinstance(nilai_baru, int):
            raise ValueError("Jumlah harus berupa bilangan bulat!")
        if nilai_baru < 0:
            raise ValueError("Jumlah tidak boleh negatif!")
        self.__jumlah = nilai_baru

    @property
    def total_diamati(self):
        return self.__total_diamati

    def tambah_populasi(self, jumlah):
        if jumlah <= 0:
            print(f"Jumlah penambahan harus positif.")
            return
        self.__jumlah += jumlah
        print(f"Populasi '{self.nama_spesies}' bertambah {jumlah}. "
              f"Total: {self.__jumlah} ekor")

    def kurangi_populasi(self, jumlah=1):
        if jumlah <= 0:
            print(f"Jumlah pengurangan harus positif.")
            return False
        if self.__jumlah < jumlah:
            print(f"Populasi '{self.nama_spesies}' tidak cukup. "
                  f"Tersedia: {self.__jumlah} ekor")
            return False
        self.__jumlah -= jumlah
        self.__total_diamati += 1
        return True

    def catat_pengamatan(self):
        self.__total_diamati += 1
        print(f"Pengamatan '{self.nama_spesies}' dicatat. "
              f"Total: {self.__total_diamati}x")

    def info(self):
        print(f"  Spesies    : {self.nama_spesies}")
        print(f"  Habitat    : {self.habitat}")
        print(f"  Suhu Ideal : {self.suhu_ideal}°C")
        print(f"  Jumlah     : {self.__jumlah} ekor")
        print(f"  Diamati    : {self.__total_diamati}x")
        print(f"  Instansi   : {HewanAkuatik.nama_instansi}")
        print("-" * 50)

    @classmethod
    def dari_dict(cls, data):
        return cls(
            data["nama_spesies"],
            data["habitat"],
            data["suhu_ideal"],
            data["jumlah"]
        )

    @classmethod
    def ubah_instansi(cls, nama_baru):
        cls.nama_instansi = nama_baru
        print(f"Nama instansi diubah menjadi: {cls.nama_instansi}")

    @classmethod
    def ubah_suhu_default(cls, suhu_baru):
        cls.suhu_ideal_default = suhu_baru
        print(f"Suhu ideal default diubah menjadi: {cls.suhu_ideal_default}°C")

    @staticmethod
    def validasi_habitat(habitat):
        habitat_valid = ["Air Tawar", "Air Laut", "Air Payau", "Air Asin"]
        return habitat in habitat_valid

    @staticmethod
    def cek_suhu_aman(suhu):
        return 20.0 <= suhu <= 35.0

    @staticmethod
    def format_angka(angka):
        return f"{angka:,}".replace(",", ".")


class Kolam:
    nama_instansi = "Balai Konservasi Perairan Mulawarman"
    total_kolam_terdaftar = 0
    kapasitas_maksimal_default = 1000

    def __init__(self, nama_kolam, lokasi, volume_liter):
        self.nama_kolam = nama_kolam
        self.lokasi = lokasi
        self.volume_liter = volume_liter
        self.__kapasitas = Kolam.kapasitas_maksimal_default
        self.__penghuni = []

        Kolam.total_kolam_terdaftar += 1

    @property
    def kapasitas(self):
        return self.__kapasitas

    @kapasitas.setter
    def kapasitas(self, nilai_baru):
        if not isinstance(nilai_baru, int):
            raise ValueError("Kapasitas harus berupa bilangan bulat!")
        if nilai_baru <= 0:
            raise ValueError("Kapasitas harus lebih dari 0!")
        self.__kapasitas = nilai_baru

    @property
    def penghuni(self):
        return self.__penghuni.copy()

    def tambah_penghuni(self, hewan):
        total_sekarang = sum(h.jumlah for h in self.__penghuni)
        if total_sekarang + hewan.jumlah > self.__kapasitas:
            print(f"Kapasitas kolam '{self.nama_kolam}' tidak cukup! "
                  f"Kapasitas: {self.__kapasitas}, Terisi: {total_sekarang}")
            return False
        self.__penghuni.append(hewan)
        print(f"'{hewan.nama_spesies}' ({hewan.jumlah} ekor) "
              f"ditambahkan ke kolam '{self.nama_kolam}'.")
        return True

    def info(self):
        total_penghuni = sum(h.jumlah for h in self.__penghuni)
        print(f"  Nama Kolam  : {self.nama_kolam}")
        print(f"  Lokasi      : {self.lokasi}")
        print(f"  Volume      : {self.volume_liter} liter")
        print(f"  Kapasitas   : {self.__kapasitas} ekor")
        print(f"  Terisi      : {total_penghuni} ekor")
        if self.__penghuni:
            print(f"  Penghuni    : {', '.join(h.nama_spesies for h in self.__penghuni)}")
        print("-" * 50)

    @classmethod
    def dari_dict(cls, data):
        return cls(data["nama_kolam"], data["lokasi"], data["volume_liter"])

    @classmethod
    def ubah_kapasitas_default(cls, nilai_baru):
        if nilai_baru <= 0:
            print("Kapasitas default harus positif!")
            return
        cls.kapasitas_maksimal_default = nilai_baru
        print(f"Kapasitas default diubah menjadi: {cls.kapasitas_maksimal_default} ekor")

    @staticmethod
    def validasi_volume(volume):
        return volume > 0

    @staticmethod
    def hitung_kepadatan(jumlah_hewan, volume_liter):
        if volume_liter <= 0:
            return 0
        return round(jumlah_hewan / volume_liter, 2)


class Peneliti:
    nama_instansi = "Balai Konservasi Perairan Mulawarman"
    total_peneliti_terdaftar = 0
    maksimal_proyek = 5

    def __init__(self, nama, nip, bidang):
        self.nama = nama
        self.nip = nip
        self.bidang = bidang
        self.__proyek_aktif = []
        self.__jam_kerja = 0

        Peneliti.total_peneliti_terdaftar += 1

    @property
    def proyek_aktif(self):
        return self.__proyek_aktif.copy()

    @property
    def jam_kerja(self):
        return self.__jam_kerja

    @jam_kerja.setter
    def jam_kerja(self, nilai):
        if nilai < 0:
            raise ValueError("Jam kerja tidak boleh negatif!")
        self.__jam_kerja = nilai

    def tambah_proyek(self, nama_proyek):
        if len(self.__proyek_aktif) >= Peneliti.maksimal_proyek:
            print(f"{self.nama} sudah mencapai batas maksimal proyek "
                  f"({Peneliti.maksimal_proyek}).")
            return False
        self.__proyek_aktif.append(nama_proyek)
        print(f"Proyek '{nama_proyek}' ditambahkan ke {self.nama}.")
        return True

    def catat_jam_kerja(self, jam):
        if jam <= 0:
            print("Jam kerja harus positif!")
            return
        self.__jam_kerja += jam
        print(f"{self.nama} mencatat {jam} jam kerja. Total: {self.__jam_kerja} jam")

    def info(self):
        print(f"  Nama        : {self.nama}")
        print(f"  NIP         : {self.nip}")
        print(f"  Bidang      : {self.bidang}")
        print(f"  Proyek      : {len(self.__proyek_aktif)}/{Peneliti.maksimal_proyek}")
        if self.__proyek_aktif:
            print(f"  Proyek aktif: {', '.join(self.__proyek_aktif)}")
        print(f"  Jam Kerja   : {self.__jam_kerja} jam")
        print("-" * 50)

    @classmethod
    def dari_dict(cls, data):
        return cls(data["nama"], data["nip"], data["bidang"])

    @classmethod
    def ubah_maksimal_proyek(cls, jumlah_baru):
        if jumlah_baru <= 0:
            print("Maksimal proyek harus positif!")
            return
        cls.maksimal_proyek = jumlah_baru
        print(f"Maksimal proyek diubah menjadi: {cls.maksimal_proyek}")

    @staticmethod
    def validasi_nip(nip):
        return nip.isdigit() and len(nip) == 8

    @staticmethod
    def validasi_nama(nama):
        return len(nama.strip()) > 0

    @staticmethod
    def hitung_produktivitas(jumlah_proyek, jam_kerja):
        if jam_kerja <= 0:
            return 0
        return round((jumlah_proyek / jam_kerja) * 100, 2)


def main():
    print("=" * 55)
    print("  SISTEM PENDATAAN HEWAN AKUATIK - DEMONSTRASI OOP")
    print("=" * 55)

    print("\nMEMBUAT OBJEK HEWAN AKUATIK\n")

    hewan1 = HewanAkuatik("Ikan Nila", "Air Tawar", 27.0, 150)
    hewan2 = HewanAkuatik("Ikan Kakap Merah", "Air Laut", 28.5, 80)

    data_hewan3 = {"nama_spesies": "Udang Vaname", "habitat": "Air Payau",
                   "suhu_ideal": 29.0, "jumlah": 200}
    hewan3 = HewanAkuatik.dari_dict(data_hewan3)

    print(f"Total hewan terdaftar: {HewanAkuatik.total_hewan_terdaftar}")

    print("\nMEMBUAT OBJEK KOLAM\n")

    kolam1 = Kolam("Kolam A1", "Lab Akuakultur", 5000)
    kolam2 = Kolam("Kolam B2", "Greenhouse Perairan", 3000)

    data_kolam3 = {"nama_kolam": "Kolam C3", "lokasi": "Area Outdoor",
                   "volume_liter": 8000}
    kolam3 = Kolam.dari_dict(data_kolam3)

    print(f"Total kolam terdaftar: {Kolam.total_kolam_terdaftar}")

    print("\nMEMBUAT OBJEK PENELITI\n")

    peneliti1 = Peneliti("Dr. Budi Santoso", "19850101", "Iktiologi")
    peneliti2 = Peneliti("Siti Aminah, M.Si", "19900202", "Limnologi")

    data_peneliti3 = {"nama": "Andi Wijaya, S.Pi", "nip": "19950303",
                      "bidang": "Akuakultur"}
    peneliti3 = Peneliti.dari_dict(data_peneliti3)

    print(f"Total peneliti terdaftar: {Peneliti.total_peneliti_terdaftar}")

    print("\nDEMONSTRASI INSTANCE METHOD\n")

    kolam1.tambah_penghuni(hewan1)
    kolam1.tambah_penghuni(hewan3)
    kolam2.tambah_penghuni(hewan2)

    print("\n--- Informasi Kolam ---")
    kolam1.info()
    kolam2.info()
    kolam3.info()

    print("\n--- Informasi Hewan Akuatik ---")
    hewan1.info()
    hewan2.info()
    hewan3.info()

    print("\n--- Demonstrasi Pengamatan & Populasi ---")
    hewan1.catat_pengamatan()
    hewan1.tambah_populasi(50)
    hewan2.kurangi_populasi(10)
    hewan2.catat_pengamatan()

    print("\n--- Demonstrasi Peneliti ---")
    peneliti1.tambah_proyek("Monitoring Ikan Nila")
    peneliti1.tambah_proyek("Konservasi Kakap")
    peneliti2.tambah_proyek("Penelitian Limnologi Danau")
    peneliti1.catat_jam_kerja(40)
    peneliti2.catat_jam_kerja(35)

    print("\n--- Info Setelah Aktivitas ---")
    hewan1.info()
    peneliti1.info()
    peneliti2.info()

    print("\nDEMONSTRASI CLASS METHOD\n")

    HewanAkuatik.ubah_instansi("Dinas Perikanan Kalimantan Timur")
    HewanAkuatik.ubah_suhu_default(28.0)
    Kolam.ubah_kapasitas_default(1500)
    Peneliti.ubah_maksimal_proyek(10)

    print(f"\nNama instansi baru: {HewanAkuatik.nama_instansi}")
    print(f"Suhu default baru: {HewanAkuatik.suhu_ideal_default}°C")
    print(f"Kapasitas default baru: {Kolam.kapasitas_maksimal_default} ekor")
    print(f"Maksimal proyek baru: {Peneliti.maksimal_proyek}")

    print("\nDEMONSTRASI STATIC METHOD\n")

    print(f"Validasi habitat 'Air Tawar': "
          f"{HewanAkuatik.validasi_habitat('Air Tawar')}")
    print(f"Validasi habitat 'Air Angkasa': "
          f"{HewanAkuatik.validasi_habitat('Air Angkasa')}")
    print(f"Cek suhu aman 27°C: {HewanAkuatik.cek_suhu_aman(27)}")
    print(f"Cek suhu aman 40°C: {HewanAkuatik.cek_suhu_aman(40)}")

    print(f"Validasi volume 5000: {Kolam.validasi_volume(5000)}")
    print(f"Validasi volume -100: {Kolam.validasi_volume(-100)}")
    print(f"Kepadatan 150 ekor / 5000 L: "
          f"{Kolam.hitung_kepadatan(150, 5000)} ekor/liter")

    print(f"Validasi NIP '19850101': {Peneliti.validasi_nip('19850101')}")
    print(f"Validasi NIP 'abc123': {Peneliti.validasi_nip('abc123')}")
    print(f"Validasi nama 'Budi': {Peneliti.validasi_nama('Budi')}")
    print(f"Validasi nama '   ': {Peneliti.validasi_nama('   ')}")
    print(f"Produktivitas 2 proyek/40 jam: "
          f"{Peneliti.hitung_produktivitas(2, 40)}")

    print("\nDEMONSTRASI GETTER & SETTER (VALIDASI)\n")

    print("--- Uji Setter Jumlah Hewan ---")
    print(f"Jumlah awal hewan1: {hewan1.jumlah} ekor")

    hewan1.jumlah = 200
    print(f"Jumlah setelah set 200: {hewan1.jumlah} ekor")

    try:
        hewan1.jumlah = -50
    except ValueError as e:
        print(f"Error: {e}")

    try:
        hewan1.jumlah = "banyak"
    except ValueError as e:
        print(f"Error: {e}")

    print("\n--- Uji Setter Kapasitas Kolam ---")
    print(f"Kapasitas awal kolam1: {kolam1.kapasitas} ekor")

    kolam1.kapasitas = 2000
    print(f"Kapasitas setelah set 2000: {kolam1.kapasitas} ekor")

    try:
        kolam1.kapasitas = 0
    except ValueError as e:
        print(f"Error: {e}")

    try:
        kolam1.kapasitas = -100
    except ValueError as e:
        print(f"Error: {e}")

    print("\n--- Uji Setter Jam Kerja Peneliti ---")
    print(f"Jam kerja awal peneliti2: {peneliti2.jam_kerja} jam")

    peneliti2.jam_kerja = 50
    print(f"Jam kerja setelah set 50: {peneliti2.jam_kerja} jam")

    try:
        peneliti2.jam_kerja = -10
    except ValueError as e:
        print(f"Error: {e}")

    print("\n" + "=" * 55)
    print("  RINGKASAN AKHIR")
    print("=" * 55)
    print(f"  Total Hewan Terdaftar   : {HewanAkuatik.total_hewan_terdaftar}")
    print(f"  Total Kolam Terdaftar   : {Kolam.total_kolam_terdaftar}")
    print(f"  Total Peneliti Terdaftar: {Peneliti.total_peneliti_terdaftar}")
    print(f"  Nama Instansi           : {HewanAkuatik.nama_instansi}")
    print(f"  Suhu Ideal Default      : {HewanAkuatik.suhu_ideal_default}°C")
    print(f"  Kapasitas Default       : {Kolam.kapasitas_maksimal_default} ekor")
    print(f"  Maksimal Proyek         : {Peneliti.maksimal_proyek}")
    print("=" * 55)
    print("  Program selesai. Terima kasih!")
    print("=" * 55)


if __name__ == "__main__":
    main()