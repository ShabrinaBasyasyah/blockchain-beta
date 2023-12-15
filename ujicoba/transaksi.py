from datetime import datetime

class Transaksi:
    def __init__(self, id, id_periode, kode_transaksi, tanggal_transaksi, id_pelaku_usaha, beli_dari_pelaku_usaha,
                 jumlah_karbon_masuk, satuan_karbon_masuk, harga_beli, nilai_beli_karbon, satuan_harga, jual_ke,
                 jumlah_karbon_keluar, satuan_karbon_keluar, harga_jual, satuan_harga_jual, nilai_jual_karbon, token,
                 saldo_emisi, satuan_saldo, saldo_nilai_ekonomi, satuan_mata_uang, token_expired, approval_status,
                 approved_by, approved_at, created_by, created_at, modified_by, is_deleted, file, id_penawaran,
                 id_permintaan, id_transaksi_origin, is_spe, is_direct_offset):
        # Initialize the attributes of the transaction
        self.id = id
        self.id_periode = id_periode
        self.kode_transaksi = kode_transaksi
        self.tanggal_transaksi = tanggal_transaksi
        self.id_pelaku_usaha = id_pelaku_usaha
        self.beli_dari_pelaku_usaha = beli_dari_pelaku_usaha
        self.jumlah_karbon_masuk = jumlah_karbon_masuk
        self.satuan_karbon_masuk = satuan_karbon_masuk
        self.harga_beli = harga_beli
        self.nilai_beli_karbon = nilai_beli_karbon
        self.satuan_harga = satuan_harga
        self.jual_ke = jual_ke
        self.jumlah_karbon_keluar = jumlah_karbon_keluar
        self.satuan_karbon_keluar = satuan_karbon_keluar
        self.harga_jual = harga_jual
        self.satuan_harga_jual = satuan_harga_jual
        self.nilai_jual_karbon = nilai_jual_karbon
        self.token = token
        self.saldo_emisi = saldo_emisi
        self.satuan_saldo = satuan_saldo
        self.saldo_nilai_ekonomi = saldo_nilai_ekonomi
        self.satuan_mata_uang = satuan_mata_uang
        self.token_expired = token_expired
        self.approval_status = approval_status
        self.approved_by = approved_by
        self.approved_at = approved_at
        self.created_by = created_by
        self.created_at = created_at
        self.modified_by = modified_by
        self.is_deleted = is_deleted
        self.file = file
        self.id_penawaran = id_penawaran
        self.id_permintaan = id_permintaan
        self.id_transaksi_origin = id_transaksi_origin
        self.is_spe = is_spe
        self.is_direct_offset = is_direct_offset

    def to_dict(self):
        return vars(self)

    @classmethod
    def from_user_input(cls):
        try:
            id_periode = input("Masukkan ID Periode: ")
            kode_transaksi = input("Masukkan Kode Transaksi: ")
            tanggal_transaksi = input("Masukkan Tanggal Transaksi (YYYY-MM-DD): ")
            tanggal_transaksi = datetime.strptime(tanggal_transaksi, "%Y-%m-%d").date()
            id_pelaku_usaha = input("Masukkan ID Pelaku Usaha: ")
            beli_dari_pelaku_usaha = input("Beli dari Pelaku Usaha (Y/N): ")
            jumlah_karbon_masuk = float(input("Masukkan Jumlah Karbon Masuk: "))
            satuan_karbon_masuk = input("Masukkan Satuan Karbon Masuk: ")
            harga_beli = float(input("Masukkan Harga Beli: "))
            nilai_beli_karbon = float(input("Masukkan Nilai Beli Karbon: "))
            satuan_harga = input("Masukkan Satuan Harga: ")
            jual_ke = input("Jual ke: ")
            jumlah_karbon_keluar = float(input("Masukkan Jumlah Karbon Keluar: "))
            satuan_karbon_keluar = input("Masukkan Satuan Karbon Keluar: ")
            harga_jual = float(input("Masukkan Harga Jual: "))
            satuan_harga_jual = input("Masukkan Satuan Harga Jual: ")
            nilai_jual_karbon = float(input("Masukkan Nilai Jual Karbon: "))
            token = input("Masukkan Token: ")
            saldo_emisi = float(input("Masukkan Saldo Emisi: "))
            satuan_saldo = input("Masukkan Satuan Saldo: ")
            saldo_nilai_ekonomi = float(input("Masukkan Saldo Nilai Ekonomi: "))
            satuan_mata_uang = input("Masukkan Satuan Mata Uang: ")
            token_expired = input("Masukkan Token Expired (Y/N): ")
            approval_status = input("Masukkan Approval Status: ")
            approved_by = input("Masukkan Approved By: ")
            approved_at = input("Masukkan Approved At (YYYY-MM-DD HH:MM:SS): ")
            approved_at = datetime.strptime(approved_at, "%Y-%m-%d %H:%M:%S")
            created_by = input("Masukkan Created By: ")
            created_at = input("Masukkan Created At (YYYY-MM-DD HH:MM:SS): ")
            created_at = datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S")
            modified_by = input("Masukkan Modified By: ")
            is_deleted = input("Masukkan Is Deleted (Y/N): ")
            file = input("Masukkan File: ")
            id_penawaran = input("Masukkan ID Penawaran: ")
            id_permintaan = input("Masukkan ID Permintaan: ")
            id_transaksi_origin = input("Masukkan ID Transaksi Origin: ")
            is_spe = input("Masukkan Is SPE (Y/N): ")
            is_direct_offset = input("Masukkan Is Direct Offset (Y/N): ")

        except ValueError as e:
            print(f"Input tidak valid: {e}")
            return None  # Add return None if a ValueError occurs

        return cls(
            id=None,
            id_periode=id_periode,
            kode_transaksi=kode_transaksi,
            tanggal_transaksi=tanggal_transaksi,
            id_pelaku_usaha=id_pelaku_usaha,
            beli_dari_pelaku_usaha=beli_dari_pelaku_usaha,
            jumlah_karbon_masuk=jumlah_karbon_masuk,
            satuan_karbon_masuk=satuan_karbon_masuk,
            harga_beli=harga_beli,
            nilai_beli_karbon=nilai_beli_karbon,
            satuan_harga=satuan_harga,
            jual_ke=jual_ke,
            jumlah_karbon_keluar=jumlah_karbon_keluar,
            satuan_karbon_keluar=satuan_karbon_keluar,
            harga_jual=harga_jual,
            satuan_harga_jual=satuan_harga_jual,
            nilai_jual_karbon=nilai_jual_karbon,
            token=token,
            saldo_emisi=saldo_emisi,
            satuan_saldo=satuan_saldo,
            saldo_nilai_ekonomi=saldo_nilai_ekonomi,
            satuan_mata_uang=satuan_mata_uang,
            token_expired=token_expired,
            approval_status=approval_status,
            approved_by=approved_by,
            approved_at=approved_at,
            created_by=created_by,
            created_at=created_at,
            modified_by=modified_by,
            is_deleted=is_deleted,
            file=file,
            id_penawaran=id_penawaran,
            id_permintaan=id_permintaan,
            id_transaksi_origin=id_transaksi_origin,
            is_spe=is_spe,
            is_direct_offset=is_direct_offset,
        )

if __name__ == "__main__":
    # Add the necessary imports and any other code outside the class here
    pass