from produk import Produk

jumlah_produk = int(input('Masukkan jumlah produk: '))

total_keseluruhan_bayar = 0

for i in range(jumlah_produk):
    print(f"\n--- Barang ke-{i+1} ---")
    nama = input('Masukkan nama produk: ')
    harga = int(input('Masukkan Harga Barang Rp. '))
    jumlah = int(input('Masukkan Jumlah Barang   : '))

    p = Produk(nama, harga)
    p.tampilkan_info()

    subtotal = p.hitung_total(jumlah)

    diskon_produk = p.hitung_diskon(subtotal)

    bayar_produk_ini = subtotal - diskon_produk
    print(f"Diskon Barang Ini: Rp{int(diskon_produk):,}")
    print(f"Harga Bersih Barang Ini: Rp{int(bayar_produk_ini):,}")

    total_keseluruhan_bayar += bayar_produk_ini
    
print("\n=== HASIL AKHIR PEMBELIAN ===")
print(f"Total Akhir Harus Dibayar ({jumlah_produk} Produk): Rp{int(total_keseluruhan_bayar):,}")
