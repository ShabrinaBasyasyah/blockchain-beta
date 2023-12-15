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
        self.sisa_penawaran = sisa_penawaran
        self.satuan_sisa_penawaran = satuan_sisa_penawaran
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