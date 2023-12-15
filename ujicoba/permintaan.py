from datetime import datetime

class Permintaan:
    def __init__(
        self,
        id,
        id_pelaku_usaha,
        id_periode,
        tanggal_permintaan,
        tanggal_awal_berlaku,
        tanggal_akhir_berlaku,
        ptbae_diminta,
        satuan,
        harga,
        mata_uang,
        jumlah_terbeli,
        satuan_terbeli,
        sisa_permintaan,
        satuan_sisa_permintaan,
        tanggal_terbeli,
        created_by,
        created_at,
        last_modified_by,
        last_modified_at,
        is_deleted,
        status,
        available_permintaan,
        is_spe,
        is_direct_offset,
    ):
        # Initialize the attributes of the request
        self.id = id
        self.id_pelaku_usaha = id_pelaku_usaha
        self.id_periode = id_periode
        self.tanggal_permintaan = tanggal_permintaan
        self.tanggal_awal_berlaku = tanggal_awal_berlaku
        self.tanggal_akhir_berlaku = tanggal_akhir_berlaku
        self.ptbae_diminta = ptbae_diminta
        self.satuan = satuan
        self.harga = harga
        self.mata_uang = mata_uang
        self.jumlah_terbeli = jumlah_terbeli
        self.satuan_terbeli = satuan_terbeli
        
        if jumlah_terbeli is not None and ptbae_diminta is not None:
            if jumlah_terbeli == ptbae_diminta:
                self.sisa_permintaan = 0
            elif 0 < jumlah_terbeli < ptbae_diminta:
                self.sisa_permintaan = ptbae_diminta - jumlah_terbeli
            else: 
                raise ValueError("Data tidak valid. Jumlah terbeli melebihi permintaan")
        else:
            self.sisa_permintaan = sisa_permintaan if sisa_permintaan is not None else 0
            self.satuan_sisa_permintaan = satuan_sisa_permintaan if satuan_sisa_permintaan is not None else ""
        self.tanggal_terbeli = tanggal_terbeli
        self.created_by = created_by
        self.created_at = created_at
        self.last_modified_by = last_modified_by
        self.last_modified_at = last_modified_at
        self.is_deleted = is_deleted
        self.status = status
        self.available_permintaan = available_permintaan
        self.is_spe = is_spe
        self.is_direct_offset = is_direct_offset

    def to_dict(self):
        return vars(self)

    @staticmethod
    def from_user_input():
        try:
            id_pelaku_usaha = input("Masukkan ID Pelaku Usaha: ")
            id_periode = input("Masukkan ID periode: ")
            tanggal_permintaan = input("Masukkan Tanggal Permintaan (YYYY-MM-DD): ")
            tanggal_permintaan = datetime.strptime(tanggal_permintaan, "%Y-%m-%d").date()

            tanggal_awal_berlaku = input("Masukkan tanggal awal berlakunya permintaan (YYYY-MM-DD): ")
            tanggal_awal_berlaku = datetime.strptime(tanggal_awal_berlaku, "%Y-%m-%d").date()

            tanggal_akhir_berlaku = input("Masukkan tanggal akhir permintaan (YYYY-MM-DD): ")
            tanggal_akhir_berlaku = datetime.strptime(tanggal_akhir_berlaku, "%Y-%m-%d").date()

            ptbae_diminta = float(input("Masukkan jumlah ptbae yang diminta: "))
            satuan = input("Satuan ptbae: ")

            harga = float(input("Masukkan harga ptbae yang diminta: "))
            mata_uang = input("Masukkan mata uang yang digunakan: ")

            jumlah_terbeli = float(input("Masukkan jumlah yang terbeli pada permintaan: "))
            satuan_terbeli = input("Satuan ptbae: ")

            sisa_permintaan = float(input("Sisa permintaan yang ada: "))
            satuan_sisa_permintaan = input("Satuan ptbae (sisa permintaan): ")

            tanggal_terbeli = input("tanggal ptbae terbeli (YYYY-MM-DD): ")
            tanggal_terbeli = datetime.strptime(tanggal_terbeli, "%Y-%m-%d").date()

            created_by = input("pembuat permintaan: ")
            created_at = input("waktu dibuat permintaan: ")
            created_at = datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S")

            last_modified_by = input("modified_by : ")
            last_modified_at = input("Modified at: ")
            last_modified_at = datetime.strptime(last_modified_at, "%Y-%m-%d %H:%M:%S")

            is_deleted = input("hapus transaksi (Y/N): ")
            status = input("status permintaan: ")
            available_permintaan = input("permintaan tersedia: ")
            is_spe = input("is_spe Y/N: ")
            is_direct_offset = input("is_direct_offset Y/N: ")

        except ValueError as e:
            print(f"Input tidak valid: {e}")
            return None  # Tambahkan return None jika terjadi ValueError

        if jumlah_terbeli is not None and ptbae_diminta is not None:
            if jumlah_terbeli == ptbae_diminta:
                sisa_permintaan = 0
            elif 0 < jumlah_terbeli < ptbae_diminta:
                sisa_permintaan = ptbae_diminta - jumlah_terbeli
            else:
                print("Data tidak valid. Jumlah terbeli tidak dapat melebihi permintaan.")
                return None  # Tambahkan return None jika data tidak valid
        else:
            print("Data tidak valid. Pastikan Anda memasukkan angka yang benar.")
            return None  # Tambahkan return None jika data tidak valid

        return Permintaan(
            id=None,
            id_pelaku_usaha=id_pelaku_usaha,
            id_periode=id_periode,
            tanggal_permintaan=tanggal_permintaan,
            tanggal_awal_berlaku=tanggal_awal_berlaku,
            tanggal_akhir_berlaku=tanggal_akhir_berlaku,
            ptbae_diminta=ptbae_diminta,
            satuan=satuan,
            harga=harga,
            mata_uang=mata_uang,
            jumlah_terbeli=jumlah_terbeli,
            satuan_terbeli=satuan_terbeli,
            sisa_permintaan=sisa_permintaan,
            satuan_sisa_permintaan=satuan_sisa_permintaan,
            tanggal_terbeli=tanggal_terbeli,
            created_by=created_by,
            created_at=created_at,
            last_modified_by=last_modified_by,
            last_modified_at=last_modified_at,
            is_deleted=is_deleted,
            status=status,
            available_permintaan=available_permintaan,
            is_spe=is_spe,
            is_direct_offset=is_direct_offset,
        )

if __name__ == "__main__":
    # Add the necessary imports and any other code outside the class here
    pass
