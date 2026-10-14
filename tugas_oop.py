class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def tampilkan_info(self):
        print(f"Nama Produk: {self.nama}, Harga: Rp {self.harga:,}")

    def hitung_total(self, jumlah):
        return self.harga * jumlah

    def hitung_diskon(self, total_pembelian):
        if total_pembelian > 5000:
            return total_pembelian * 0.05
        return 0
