class KarakterSurfer:
    def __init__(self, nama):
        self.nama = nama
        self.skor = 0
        self.koin = 0
        self.is_running = True

    def berlari(self):
        self.is_running = True
        print(self.nama, "lagi lari ngebut menghindari inspektur!")

    def ambil_koin(self, jumlah):
        self.koin += jumlah
        print(f"Asik dapet {jumlah} koin! Total koin sekarang: {self.koin}")

    def tabrak_rintangan(self):
        self.is_running = False
        print("Duh ketangkep! " + self.nama + " nabrak rintangan, Game Over!")

    def info_player(self):
        print("STATUS PLAYER")
        print("Nama:", self.nama)
        print("Skor:", self.skor)
        print("Koin:", self.koin)
        print("Lagi lari:", self.is_running)
        
# --- PENGUJIAN OBJEK ---
player1 = KarakterSurfer("Jake")

player1.info_player()
player1.berlari()
player1.ambil_koin(15)
player1.ambil_koin(50)
player1.info_player()
player1.tabrak_rintangan()
player1.info_player()