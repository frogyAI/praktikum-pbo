from abc import ABC, abstractmethod


class HewanAkuatik(ABC):
    nama_instansi = "Balai Konservasi Perairan Mulawarman"
    total_hewan_terdaftar = 0
    suhu_ideal_default = 27.0

    def __init__(self, nama_spesies, habitat, suhu_ideal, jumlah):
        self.nama_spesies = nama_spesies
        self.habitat = habitat
        self.suhu_ideal = suhu_ideal
        self._kode_identifikasi = f"HW-{nama_spesies[:3].upper()}"
        self.__jumlah = jumlah
        self.__total_diamati = 0

        HewanAkuatik.total_hewan_terdaftar += 1

    @abstractmethod
    def bersuara(self):
        pass

    @abstractmethod
    def bergerak(self):
        pass

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

    def __str__(self):
        return f"{self.nama_spesies} ({self.habitat}, {self.__jumlah} ekor)"

    def __add__(self, other):
        if isinstance(other, HewanAkuatik):
            return self.__jumlah + other.__jumlah
        return NotImplemented

    def __eq__(self, other):
        if not isinstance(other, HewanAkuatik):
            return NotImplemented
        return (self.nama_spesies == other.nama_spesies and
                self.habitat == other.habitat)

    def __lt__(self, other):
        if not isinstance(other, HewanAkuatik):
            return NotImplemented
        return self.__jumlah < other.__jumlah

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


class Ikan(HewanAkuatik):
    def __init__(self, nama_spesies, habitat, suhu_ideal, jumlah,
                 jenis_air, bentuk_tubuh):
        super().__init__(nama_spesies, habitat, suhu_ideal, jumlah)
        self.__nomor_registrasi = f"REG-IK-{id(self) % 10000}"
        self.jenis_air = jenis_air
        self.bentuk_tubuh = bentuk_tubuh

    def bersuara(self):
        return f"{self.nama_spesies}: Blub blub..."

    def bergerak(self):
        return f"{self.nama_spesies} berenang dengan sirip"

    def get_nomor_registrasi(self):
        return self.__nomor_registrasi

    def info(self):
        super().info()
        print(f"  [IKAN] Kode ID    : {self._kode_identifikasi}")
        print(f"  [IKAN] No. Reg    : {self.__nomor_registrasi}")
        print(f"  [IKAN] Jenis Air  : {self.jenis_air}")
        print(f"  [IKAN] Bentuk     : {self.bentuk_tubuh}")
        print("-" * 50)


class Krustasea(HewanAkuatik):
    def __init__(self, nama_spesies, habitat, suhu_ideal, jumlah,
                 memiliki_cangkang, jumlah_kaki):
        super().__init__(nama_spesies, habitat, suhu_ideal, jumlah)
        self.__nomor_registrasi = f"REG-KR-{id(self) % 10000}"
        self.memiliki_cangkang = memiliki_cangkang
        self.jumlah_kaki = jumlah_kaki

    def bersuara(self):
        return f"{self.nama_spesies}: Klik klik..."

    def bergerak(self):
        return f"{self.nama_spesies} merayap di dasar perairan"

    def get_nomor_registrasi(self):
        return self.__nomor_registrasi

    def info(self):
        super().info()
        print(f"  [KRUSTASEA] Kode ID   : {self._kode_identifikasi}")
        print(f"  [KRUSTASEA] No. Reg   : {self.__nomor_registrasi}")
        print(f"  [KRUSTASEA] Cangkang  : {'Ya' if self.memiliki_cangkang else 'Tidak'}")
        print(f"  [KRUSTASEA] Kaki      : {self.jumlah_kaki} pasang")
        print("-" * 50)


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

    def deskripsi(self):
        return f"{self.nama_kolam} di {self.lokasi}, volume {self.volume_liter} L"

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

    def deskripsi(self):
        return f"{self.nama}, bidang {self.bidang}"

    def info(self):
        print(f"  Nama        : {self.nama}")
        print(f"  NIP         : {self.nip}")
        print(f"  Bidang      : {self.bidang}")
        print(f"  Proyek      : {len(self.__proyek_aktif)}/{Peneliti.maksimal_proyek}")
        if self.__proyek_aktif:
            print(f"  Proyek aktif: {', '.join(self.__proyek_aktif)}")
        print(f"  Jam Kerja   : {self.__jam_kerja} jam")
        print("-" * 50)


class PenelitiAkuatik(Peneliti):
    def __init__(self, nama, nip, bidang, spesialisasi):
        super().__init__(nama, nip, bidang)
        self.spesialisasi = spesialisasi
        self.objek_penelitian = []

    def teliti(self, hewan):
        self.objek_penelitian.append(hewan)
        print(f"{self.nama} sedang meneliti '{hewan.nama_spesies}' "
              f"(bidang: {self.spesialisasi})")

    def info(self):
        super().info()
        if self.objek_penelitian:
            nama_hewan = ", ".join(h.nama_spesies for h in self.objek_penelitian)
            print(f"  Spesialisasi   : {self.spesialisasi}")
            print(f"  Objek Diteliti : {nama_hewan}")
        print("-" * 50)


class KolamAgregasi(Kolam):
    def __init__(self, nama_kolam, lokasi, volume_liter):
        super().__init__(nama_kolam, lokasi, volume_liter)
        self.daftar_hewan_agregasi = []

    def tambah_hewan(self, hewan):
        self.daftar_hewan_agregasi.append(hewan)
        print(f"[AGREGASI] '{hewan.nama_spesies}' dimasukkan ke "
              f"kolam '{self.nama_kolam}' (referensi saja).")

    def info(self):
        super().info()
        if self.daftar_hewan_agregasi:
            print(f"  [AGREGASI] Hewan Terkait: "
                  f"{', '.join(h.nama_spesies for h in self.daftar_hewan_agregasi)}")
        print("-" * 50)


class Laboratorium:
    def __init__(self, nama_lab, kapasitas_peneliti):
        self.nama_lab = nama_lab
        self.kapasitas_peneliti = kapasitas_peneliti
        self.daftar_peneliti = []

    def tambah_peneliti(self, peneliti):
        if len(self.daftar_peneliti) >= self.kapasitas_peneliti:
            print(f"Lab '{self.nama_lab}' penuh!")
            return False
        self.daftar_peneliti.append(peneliti)
        print(f"{peneliti.nama} ditempatkan di lab '{self.nama_lab}'.")
        return True

    def info(self):
        print(f"  [LAB] {self.nama_lab} | Kapasitas: "
              f"{len(self.daftar_peneliti)}/{self.kapasitas_peneliti}")
        for p in self.daftar_peneliti:
            print(f"        - {p.nama} ({p.bidang})")


class InstansiKonservasi:
    def __init__(self, nama_instansi, alamat):
        self.nama_instansi = nama_instansi
        self.alamat = alamat
        self.__daftar_lab = []

    def tambah_lab(self, nama_lab, kapasitas):
        lab = Laboratorium(nama_lab, kapasitas)
        self.__daftar_lab.append(lab)
        print(f"Lab '{nama_lab}' dibuat di dalam instansi '{self.nama_instansi}'.")
        return lab

    def info(self):
        print(f"\n[INSTANSI] {self.nama_instansi} — {self.alamat}")
        print(f"  Jumlah Lab: {len(self.__daftar_lab)}")
        for lab in self.__daftar_lab:
            lab.info()
        print("-" * 50)


def cetak_deskripsi(obj):
    print(obj.deskripsi())


def main():
    print("=" * 55)
    print("  SISTEM PENDATAAN HEWAN AKUATIK")
    print("=" * 55)

    print("\nBUKTI ABSTRACT CLASS TIDAK DAPAT DIINSTANSIASI\n")
    try:
        hewan_abstrak = HewanAkuatik("Ikan X", "Air Tawar", 27.0, 10)
    except TypeError as e:
        print(f"TypeError: {e}")

    print("\nMEMBUAT OBJEK HEWAN AKUATIK\n")
    ikan1 = Ikan("Ikan Nila", "Air Tawar", 27.0, 150, "Tawar", "Pipih")
    ikan2 = Ikan("Ikan Kakap Merah", "Air Laut", 28.5, 80, "Asin", "Pipih")
    krust1 = Krustasea("Udang Vaname", "Air Payau", 29.0, 200, True, 5)
    krust2 = Krustasea("Kepiting Bakau", "Air Payau", 28.0, 40, True, 4)

    print(f"Total hewan terdaftar: {HewanAkuatik.total_hewan_terdaftar}")

    print("\nMEMBUAT OBJEK KOLAM & PENELITI\n")
    kolam1 = Kolam("Kolam A1", "Lab Akuakultur", 5000)
    peneliti1 = Peneliti("Dr. Budi Santoso", "19850101", "Iktiologi")
    peneliti2 = Peneliti("Siti Aminah, M.Si", "19900202", "Limnologi")

    kolam1.tambah_penghuni(ikan1)
    kolam1.tambah_penghuni(krust1)

    print("\n--- Info Ikan ---")
    ikan1.info()
    print("\n--- Info Krustasea ---")
    krust1.info()
    print("\n--- Info Kolam ---")
    kolam1.info()

    print("\n" + "=" * 55)
    print("  POLIMORFISME VIA PEWARISAN")
    print("=" * 55)
    daftar_hewan = [ikan1, krust1, ikan2, krust2]
    for hewan in daftar_hewan:
        print(hewan.bersuara())
        print(f"  -> {hewan.bergerak()}")

    print("\n" + "=" * 55)
    print("  DUCK TYPING")
    print("=" * 55)
    cetak_deskripsi(kolam1)
    cetak_deskripsi(peneliti1)
    cetak_deskripsi(peneliti2)

    print("\n" + "=" * 55)
    print("  OPERATOR OVERLOADING")
    print("=" * 55)
    print(f"str(ikan1)         : {ikan1}")
    print(f"str(krust1)        : {krust1}")
    print(f"ikan1 + krust1     : {ikan1 + krust1} ekor")
    print(f"ikan1 == ikan2     : {ikan1 == ikan2}")
    print(f"ikan1 < krust1     : {ikan1 < krust1}")
    print(f"krust1 > ikan2     : {krust1 > ikan2}")

    print("\n" + "=" * 55)
    print("  RELASI ASOSIASI")
    print("=" * 55)
    peneliti_ahli = PenelitiAkuatik("Dr. Rina", "19990101", "Iktiologi", "Genetika Ikan")
    peneliti_ahli.teliti(ikan1)
    peneliti_ahli.teliti(krust1)
    peneliti_ahli.info()

    print("\n" + "=" * 55)
    print("  RELASI AGREGASI")
    print("=" * 55)
    kolam_agregasi = KolamAgregasi("Kolam Riset A", "Lab Riset", 6000)
    kolam_agregasi.tambah_hewan(ikan1)
    kolam_agregasi.tambah_hewan(krust1)
    kolam_agregasi.info()
    del kolam_agregasi
    print(">> KolamAgregasi dihapus, tetapi ikan1 & krust1 masih hidup:")
    print(f"   ikan1  = {ikan1.nama_spesies}")
    print(f"   krust1 = {krust1.nama_spesies}")

    print("\n" + "=" * 55)
    print("  RELASI KOMPOSISI")
    print("=" * 55)
    instansi = InstansiKonservasi("Balai Konservasi Perairan Mulawarman",
                                  "Samarinda, Kaltim")
    lab1 = instansi.tambah_lab("Lab Akuakultur", 3)
    lab2 = instansi.tambah_lab("Lab Limnologi", 2)
    lab1.tambah_peneliti(peneliti_ahli)
    lab1.tambah_peneliti(peneliti1)
    lab2.tambah_peneliti(peneliti2)
    instansi.info()
    del instansi
    print(">> Instansi dihapus, seluruh laboratorium ikut hilang.")

    print("\n" + "=" * 55)
    print("  RINGKASAN AKHIR")
    print("=" * 55)
    print(f"  Total Hewan Terdaftar   : {HewanAkuatik.total_hewan_terdaftar}")
    print(f"  Total Kolam Terdaftar   : {Kolam.total_kolam_terdaftar}")
    print(f"  Total Peneliti Terdaftar: {Peneliti.total_peneliti_terdaftar}")
    print(f"  Nama Instansi           : {HewanAkuatik.nama_instansi}")
    print("=" * 55)
    print("  Program selesai. Terima kasih!")
    print("=" * 55)


if __name__ == "__main__":
    main()