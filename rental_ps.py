class RentalPS:
    def __init__(self, nama_penyewa, tipe_ps, harga_per_jam):
        self.nama_penyewa = nama_penyewa
        self.tipe_ps = tipe_ps
        self.harga_per_jam = harga_per_jam
        self.durasi = 1 
        self.is_main = False

    def mulai_main(self):
        self.is_main = True
        print("Billing dibuka!", self.nama_penyewa, "mulai main", self.tipe_ps)

    def tambah_jam(self, jam):
        if self.is_main == True:
            self.durasi += jam
            print(self.nama_penyewa, "nambah waktu", jam, "jam. Total durasi:", self.durasi, "jam")
        else:
            print("Billing belum jalan, ga bisa nambah jam!")

    def stop_main(self):
        self.is_main = False
        total = self.durasi * self.harga_per_jam
        print("\nBilling stop untuk", self.nama_penyewa)
        print("Total bayar: Rp", total)

    def info_billing(self):
        print("INFORMASI BILLING")
        print("Nama Pelanggan :", self.nama_penyewa)
        print("Tipe PS        :", self.tipe_ps)
        print("Durasi Main    :", self.durasi, "Jam")
        print("Harga / Jam    : Rp", self.harga_per_jam)
        print("Status         :", "Masih Main" if self.is_main else "Selesai / Off")


# --- PENGUJIAN OBJEK ---
rental1 = RentalPS("Zhidan", "PS5", 10000)
rental1.info_billing()
rental1.mulai_main()
rental1.tambah_jam(2)
rental1.info_billing()
rental1.stop_main()