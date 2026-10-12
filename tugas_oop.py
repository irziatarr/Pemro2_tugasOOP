class Produk:
    def __init__(self, nama, harga):

        self.nama = nama
        self.harga = harga

    def tampilkan_info(self):
        print(f"Nama Produk  : {self.nama}")
        print(f"Harga Produk : Rp{int(self.harga):,}".replace(",", "."))

    def hitung_total_produk(self, jumlah_beli):
        return self.harga * jumlah_beli

    def hitung_diskon(total_seluruh):
        if total_seluruh > 5000:
            return total_seluruh * 0.05
        return 0

def format_rupiah(nominal):
    return f"Rp{int(nominal):,}".replace(",", ".")


def main():
    print("=== PROGRAM SISTEM PEMBELIAN PRODUK ===")

    jumlah_produk = int(input("Masukkan jumlah produk yang akan dibeli: "))

    total_seluruh_pembelian = 0

    for i in range(1, jumlah_produk + 1):
        print(f"\n--- Data Produk ke-{i} ---")
        
        nama_produk = input("Nama produk : ")
        harga_produk = float(input("Harga produk: "))
        jumlah_beli = int(input("Jumlah beli : "))

        produk = Produk(nama_produk, harga_produk)

        total_produk = produk.hitung_total_produk(jumlah_beli)
        total_seluruh_pembelian += total_produk

        print(f"Total Pembelian {nama_produk}: {format_rupiah(total_produk)}")

    diskon = Produk.hitung_diskon(total_seluruh_pembelian)
    total_bayar = total_seluruh_pembelian - diskon

    print("\n=== HASIL PEMBELIAN ===")
    print(f"Total Pembelian: {format_rupiah(total_seluruh_pembelian)}")
    print(f"Diskon 5%      : {format_rupiah(diskon)}")
    print(f"Total Bayar    : {format_rupiah(total_bayar)}")


if __name__ == "__main__":
    main()