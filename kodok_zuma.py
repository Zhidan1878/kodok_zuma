class KatakZuma:
    def __init__(self, warna_awal):
        self.warna_peluru = warna_awal
        self.skor = 0
        self.is_active = True

    def ganti_warna(self, warna_baru):
        self.warna_peluru = warna_baru
        print(f"[Aksi] Warna peluru berhasil diganti menjadi: {self.warna_peluru}")

    def tembak(self):
        if self.is_active:
            self.skor += 50
            print(f"[Aksi] Bola {self.warna_peluru} ditembakkan! Skor bertambah +50.")
        else:
            print("[Aksi] Katak sedang tidak aktif, tidak dapat menembak.")

    def info_status(self):
        status_teks = "Aktif" if self.is_active else "Tidak Aktif"
        print("=== STATUS KATAK ZUMA ===")
        print(f"Warna Peluru : {self.warna_peluru}")
        print(f"Total Skor   : {self.skor}")
        print(f"Status Aktif : {status_teks} ({self.is_active})")
        print("=========================\n")

katak_player = KatakZuma("Biru")

print("--- Kondisi Awal ---")
katak_player.info_status()

katak_player.ganti_warna("Merah")

katak_player.tembak()

print("\n--- Kondisi Setelah Perubahan ---")
katak_player.info_status()