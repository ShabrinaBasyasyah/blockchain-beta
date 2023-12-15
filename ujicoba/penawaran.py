from datetime import datetime

class Penawaran:
    def __init__(
        self,
        id,
        id_pelaku_usaha,
        id_periode,
        tanggal_penawaran,
        tanggal_awal_berlaku,
        tanggal_akhir_berlaku,
        ptbae_ditawarkan,
        satuan,
        harga,
        mata_uang,
        jumlah_terjual,
        satuan_terjual,
        sisa_penawaran,
        satuan_sisa_penawaran,
        tanggal_terjual,
        created_by,
        created_at,
        last_modified_by,
        last_modified_at,
        is_deleted,
        status,
        available_penawaran,
        is_spe,
    ):
        # Initialize the attributes of the offer
        self.id = id
        self.id_pelaku_usaha = id_pelaku_usaha
        self.id_periode = id_periode
        self.tanggal_penawaran = tanggal_penawaran
        self.tanggal_awal_berlaku = tanggal_awal_berlaku
        self.tanggal_akhir_berlaku = tanggal_akhir_berlaku
        self.ptbae_ditawarkan = ptbae_ditawarkan
        self.satuan = satuan
        self.harga = harga
        self.mata_uang = mata_uang
        self.jumlah_terjual = jumlah_terjual
        self.satuan_terjual = satuan_terjual

        if jumlah_terjual is not None and ptbae_ditawarkan is not None:
            if jumlah_terjual == ptbae_ditawarkan:
                self.sisa_penawaran = 0
            elif 0 < jumlah_terjual < ptbae_ditawarkan:
                self.sisa_penawaran = ptbae_ditawarkan - jumlah_terjual
            else:
                raise ValueError("Data tidak valid. Jumlah terjual tidak dapat melebihi ptbae yang ditawarkan.")
        else:
            self.sisa_penawaran = sisa_penawaran if sisa_penawaran is not None else 0
            self.satuan_sisa_penawaran = satuan_sisa_penawaran if satuan_sisa_penawaran is not None else ""

        # Lanjutan inisialisasi atribut lainnya
        self.tanggal_terjual = tanggal_terjual
        self.created_by = created_by
        self.created_at = created_at
        self.last_modified_by = last_modified_by
        self.last_modified_at = last_modified_at
        self.is_deleted = is_deleted
        self.status = status
        self.available_penawaran = available_penawaran
        self.is_spe = is_spe

    def to_dict(self):
        return vars(self)

    @classmethod
    def from_user_input():
        try:
            id_pelaku_usaha = input("Masukkan ID Pelaku Usaha: ")
            id_periode = input("Masukkan ID periode: ")
            tanggal_penawaran = input("Masukkan Tanggal Penawaran (YYYY-MM-DD): ")
            tanggal_penawaran = datetime.strptime(tanggal_penawaran, "%Y-%m-%d").date()

            tanggal_awal_berlaku = input("Masukkan tanggal awal berlakunya penawaran (YYYY-MM-DD): ")
            tanggal_awal_berlaku = datetime.strptime(tanggal_awal_berlaku, "%Y-%m-%d").date()

            tanggal_akhir_berlaku = input("Masukkan tanggal akhir penawaran (YYYY-MM-DD): ")
            tanggal_akhir_berlaku = datetime.strptime(tanggal_akhir_berlaku, "%Y-%m-%d").date()

            ptbae_ditawarkan = float(input("Masukkan jumlah ptbae yang ditawarkan: "))

            satuan = input("Satuan ptbae (hanya dapat memasukkan 'ton co2 e'): ").lower()
            if satuan != "ton co2 e":
                raise ValueError("Satuan yang dimasukkan tidak valid. Harap masukkan 'ton co2 e'.")

            harga = float(input("Masukkan harga ptbae yang ditawarkan: "))
            mata_uang = input("Masukkan mata uang yang digunakan: ")

            # Ensure numeric input for the following fields
            jumlah_terjual = float(input("Masukkan jumlah yang terjual pada penawaran: "))
            sisa_penawaran = float(input("Sisa penawaran yang ada: "))
            available_penawaran = float(input("Penawaran tersedia: "))

            satuan_terjual = input("Satuan ptbae: ")
            satuan_sisa_penawaran = input("Satuan ptbae (sisa penawaran): ")
            tanggal_terjual = input("Tanggal ptbae terjual (YYYY-MM-DD): ")
            tanggal_terjual = datetime.strptime(tanggal_terjual, "%Y-%m-%d").date()

            created_by = input("Pembuat penawaran: ")
            created_at = input("Waktu dibuat penawaran (YYYY-MM-DD HH:MM:SS): ")
            created_at = datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S")

            last_modified_by = input("Modified by: ")
            last_modified_at = input("Modified at (YYYY-MM-DD HH:MM:SS): ")
            last_modified_at = datetime.strptime(last_modified_at, "%Y-%m-%d %H:%M:%S")

            is_deleted = input("Hapus transaksi (Y/N): ")
            status = input("Status penawaran: ")
            is_spe = input("Is_spe Y/N: ")

        except ValueError as e:
            print(f"Input tidak valid: {e}")
            return None  # Tambahkan return None jika terjadi ValueError

        if jumlah_terjual is not None and ptbae_ditawarkan is not None:
            if jumlah_terjual == ptbae_ditawarkan:
                sisa_penawaran = 0
            elif 0 < jumlah_terjual < ptbae_ditawarkan:
                sisa_penawaran = ptbae_ditawarkan - jumlah_terjual
            else:
                print("Data tidak valid. Jumlah terjual tidak dapat melebihi ptbae yang ditawarkan.")
                return None  # Tambahkan return None jika data tidak valid
        else:
            print("Data tidak valid. Pastikan Anda memasukkan angka yang benar.")
            return None  # Tambahkan return None jika data tidak valid

        return Penawaran(
            id=None,
            id_pelaku_usaha=id_pelaku_usaha,
            id_periode=id_periode,
            tanggal_penawaran=tanggal_penawaran,
            tanggal_awal_berlaku=tanggal_awal_berlaku,
            tanggal_akhir_berlaku=tanggal_akhir_berlaku,
            ptbae_ditawarkan=ptbae_ditawarkan,
            satuan=satuan,
            harga=harga,
            mata_uang=mata_uang,
            jumlah_terjual=jumlah_terjual,
            satuan_terjual=satuan_terjual,
            sisa_penawaran=sisa_penawaran,
            satuan_sisa_penawaran=satuan_sisa_penawaran,
            tanggal_terjual=tanggal_terjual,
            created_by=created_by,
            created_at=created_at,
            last_modified_by=last_modified_by,
            last_modified_at=last_modified_at,
            is_deleted=is_deleted,
            status=status,
            available_penawaran=available_penawaran,
            is_spe=is_spe,
        )

if __name__ == "__main__":
    # Add the necessary imports and any other code outside the class here
    pass