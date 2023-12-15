class Transaksi:

    def __init__(
        self,
        id,
        id_periode,
        kode_transaksi,
        tanggal_transaksi,
        id_pelaku_usaha,
        beli_dari_pelaku_usaha,
        jumlah_karbon_masuk,
        satuan_karbon_masuk,
        harga_beli,
        nilai_beli_karbon,
        satuan_harga,
        jual_ke,
        jumlah_karbon_keluar,
        satuan_karbon_keluar,
        harga_jual,
        satuan_harga_jual,
        nilai_jual_karbon,
        token,
        saldo_emisi,
        satuan_saldo,
        saldo_nilai_ekonomi,
        satuan_mata_uang,
        token_expired,
        approval_status,
        approved_by,
        approved_at,
        created_by,
        created_at,
        modified_by,
        is_deleted,
        file,
        id_penawaran,
        id_permintaan,
        id_transaksi_origin,
        is_spe,
        is_direct_offset,
    ):
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

