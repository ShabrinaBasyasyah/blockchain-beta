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
        user,
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
        self.sisa_permintaan = sisa_permintaan
        self.satuan_sisa_permintaan = satuan_sisa_permintaan
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
        self.user = user

    def to_dict(self):
        return vars(self)