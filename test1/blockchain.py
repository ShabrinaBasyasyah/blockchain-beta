import hashlib
import json
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

    def to_dict(self):
        return vars(self)

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

    def to_dict(self):
        return vars(self)

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_encoded = json.dumps(self.data, sort_keys=True).encode()
        return hashlib.sha256(str(self.timestamp).encode() + data_encoded + str(self.previous_hash).encode()).hexdigest()

    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "hash": self.hash
        }

class Blockchain:
    def __init__(self):
        self.blocks = []
        self.genesis_block = Block(0, {"permintaan": {}}, "0")
        self.blocks.append(self.genesis_block)

    def add_block(self, data):
        if isinstance(data, Permintaan):
            data_dict = data.to_dict()
            new_block = Block(datetime.now().timestamp(), data_dict, self.blocks[-1].hash)
            new_block.hash = new_block.calculate_hash()
            self.blocks.append(new_block)
        elif isinstance(data, Penawaran):
            data_dict = data.to_dict()
            new_block = Block(datetime.now().timestamp(), {"penawaran": data_dict}, self.blocks[-1].hash)
            new_block.hash = new_block.calculate_hash()
            self.blocks.append(new_block)
        elif isinstance(data, Transaksi):
            data_dict = data.to_dict()
            new_block = Block(datetime.now().timestamp(), {"transaksi": data_dict}, self.blocks[-1].hash)
            new_block.hash = new_block.calculate_hash()
            self.blocks.append(new_block)
        else:
            raise ValueError("Data yang diberikan harus berupa objek permintaan, penawaran, atau transaksi")

    def get_latest_block(self):
        return self.blocks[-1]

    def calculate_total_emissions(self):
        total_emissions = 0
        for block in self.blocks:
            if "permintaan" in block.data and "ptbae_diminta" in block.data["permintaan"]:
                total_emissions += block.data["permintaan"]["ptbae_diminta"]
            elif "penawaran" in block.data and "ptbae_ditawarkan" in block.data["penawaran"]:
                total_emissions += block.data["penawaran"]["ptbae_ditawarkan"]
            elif "transaksi" in block.data and "jumlah_karbon_masuk" in block.data["transaksi"]:
                total_emissions += block.data["transaksi"]["jumlah_karbon_masuk"]
        return total_emissions

    def add_transaksi(self, transaksi):
        if isinstance(transaksi, Transaksi):
            transaksi_dict = transaksi.to_dict()
            new_block = Block(datetime.now().timestamp(), {"transaksi": transaksi_dict}, self.blocks[-1].hash)
            new_block.hash = new_block.calculate_hash()
            self.blocks.append(new_block)
        else:
            raise ValueError("Data yang diberikan harus berupa objek Transaksi")
    
    def to_dict(self):
        return {
            "blocks": [block.to_dict() for block in self.blocks],
            "total_emissions": self.calculate_total_emissions()
        }

    def __repr__(self):
        return f"Blockchain(blocks=[\n" + "\n".join(
            [
                f"    Block(timestamp={block.timestamp}, data={block.data}, previous_hash={block.previous_hash})"
                for block in self.blocks
            ]
        ) + f"\n], total_emissions={self.calculate_total_emissions()}"

def main():
    # Membuat objek blockchain
    blockchain = Blockchain()

    while True:
        # Menampilkan menu aktivitas
        print("\nPilih jenis aktivitas:")
        print("1. Permintaan")
        print("2. Penawaran")
        print("3. Transaksi")
        print("4. Lihat Blockchain")
        print("5. Keluar")

        # Meminta pengguna untuk memilih jenis aktivitas
        choice = input("Masukkan nomor aktivitas (1-4): ")

        if choice == "1":
            # Meminta pengguna untuk memasukkan data permintaan
            print("\nMasukkan data permintaan:")
            id_permintaan = int(input("ID Permintaan: "))
            id_pelaku_usaha = int(input("ID Pelaku Usaha: "))
            id_periode = int(input("ID Periode: "))
            tanggal_permintaan = input("Tanggal Permintaan: ")
            tanggal_awal_berlaku = input("Tanggal Awal Berlaku: ")
            tanggal_akhir_berlaku = input("Tanggal Akhir Berlaku: ")
            ptbae_diminta = float(input("PTBAE Diminta: "))
            satuan_permintaan = input("Satuan Permintaan: ")
            harga_permintaan = float(input("Harga Permintaan: "))
            # Additional fields
            mata_uang = input("Mata Uang: ")
            jumlah_terbeli = float(input("Jumlah Terbeli: "))
            satuan_terbeli = input("Satuan Terbeli: ")
            sisa_permintaan = float(input("Sisa Permintaan: "))
            satuan_sisa_permintaan = input("Satuan Sisa Permintaan: ")
            tanggal_terbeli = input("Tanggal Terbeli: ")
            created_by = input("Created By: ")
            created_at = input("Created At: ")
            last_modified_by = input("Last Modified By: ")
            last_modified_at = input("Last Modified At: ")
            is_deleted = input("Is Deleted: ")
            status = input("Status: ")
            available_permintaan = float(input("Available Permintaan: "))
            is_spe = input("Is SPE: ")
            is_direct_offset = input("Is Direct Offset: ")
            

            # Membuat objek Permintaan berdasarkan input pengguna
            permintaan = Permintaan(
                id=id_permintaan,
                id_pelaku_usaha=id_pelaku_usaha,
                id_periode=id_periode,
                tanggal_permintaan=tanggal_permintaan,
                tanggal_awal_berlaku=tanggal_awal_berlaku,
                tanggal_akhir_berlaku=tanggal_akhir_berlaku,
                ptbae_diminta=ptbae_diminta,
                satuan=satuan_permintaan,
                harga=harga_permintaan,
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
            
            # Menambahkan blok baru dengan data permintaan
            blockchain.add_block(permintaan)

        elif choice == "2":
            # Meminta pengguna untuk memasukkan data penawaran
            print("\nMasukkan data penawaran:")
            id_penawaran = int(input("ID Penawaran: "))
            id_pelaku_usaha = int(input("ID Pelaku Usaha: "))
            id_periode = int(input("ID Periode: "))
            tanggal_penawaran = input("Tanggal Penawaran: ")
            tanggal_awal_berlaku = input("Tanggal Awal Berlaku: ")
            tanggal_akhir_berlaku = input("Tanggal Akhir Berlaku: ")
            ptbae_ditawarkan = float(input("PTBAE Ditawarkan: "))
            satuan = input("Satuan: ")
            harga = float(input("Harga: "))
            mata_uang = input("Mata Uang: ")
            jumlah_terjual = float(input("Jumlah Terjual: "))
            satuan_terjual = input("Satuan Terjual: ")
            sisa_penawaran = float(input("Sisa Penawaran: "))
            satuan_sisa_penawaran = input("Satuan Sisa Penawaran: ")
            tanggal_terjual = input("Tanggal Terjual: ")
            created_by = input("Created By: ")
            created_at = input("Created At: ")
            last_modified_by = input("Last Modified By: ")
            last_modified_at = input("Last Modified At: ")
            is_deleted = input("Is Deleted: ")
            status = input("Status: ")
            available_penawaran = float(input("Available Penawaran: "))
            is_spe = input("Is SPE: ")

            # Membuat objek Penawaran berdasarkan input pengguna
            penawaran = Penawaran(
                id=id_penawaran,
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

            # Menambahkan blok baru dengan data penawaran
            blockchain.add_block(penawaran)

        elif choice == "3":
            # Meminta pengguna untuk memasukkan data transaksi
            print("\nMasukkan data transaksi:")
            id_transaksi = int(input("ID Transaksi: "))
            id_periode = int(input("ID Periode: "))
            kode_transaksi = input("Kode Transaksi: ")
            tanggal_transaksi = input("Tanggal Transaksi: ")
            id_pelaku_usaha = int(input("ID Pelaku Usaha: "))
            beli_dari_pelaku_usaha = int(input("Beli dari Pelaku Usaha: "))
            jumlah_karbon_masuk = float(input("Jumlah Karbon Masuk: "))
            satuan_karbon_masuk = input("Satuan Karbon Masuk: ")
            harga_beli = float(input("Harga Beli: "))
            nilai_beli_karbon = float(input("Nilai Beli Karbon: "))
            satuan_harga = input("Satuan Harga: ")
            jual_ke = int(input("Jual ke: "))
            jumlah_karbon_keluar = float(input("Jumlah Karbon Keluar: "))
            satuan_karbon_keluar = input("Satuan Karbon Keluar: ")
            harga_jual = float(input("Harga Jual: "))
            satuan_harga_jual = input("Satuan Harga Jual: ")
            nilai_jual_karbon = float(input("Nilai Jual Karbon: "))
            token = input("Token: ")
            saldo_emisi = float(input("Saldo Emisi: "))
            satuan_saldo = input("Satuan Saldo: ")
            saldo_nilai_ekonomi = float(input("Saldo Nilai Ekonomi: "))
            satuan_mata_uang = input("Satuan Mata Uang: ")
            token_expired = input("Token Expired: ")
            approval_status = input("Approval Status: ")
            approved_by = input("Approved By: ")
            approved_at = input("Approved At: ")
            created_by = input("Created By: ")
            created_at = input("Created At: ")
            modified_by = input("Modified By: ")
            is_deleted = input("Is Deleted: ")
            file = input("File: ")
            id_penawaran = int(input("ID Penawaran: "))
            id_permintaan = int(input("ID Permintaan: "))
            id_transaksi_origin = int(input("ID Transaksi Origin: "))
            is_spe = input("Is SPE: ")
            is_direct_offset = input("Is Direct Offset: ")

            # Membuat objek Transaksi berdasarkan input pengguna
            transaksi = Transaksi(
                id=id_transaksi,
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
                is_direct_offset=is_direct_offset
            )

            # Menambahkan blok baru dengan data transaksi
            blockchain.add_transaksi(transaksi)


        elif choice == "4":
           # Menampilkan seluruh blockchain
            print("\nBlockchain:")
            print(blockchain.to_dict())


        elif choice == "5":
            # Keluar dari program
            break

        else:
            print("Pilihan tidak valid. Silakan masukkan nomor aktivitas yang benar.")
        
    # Cetak blockchain setelah keluar dari loop
    print("\nBlockchain:")
    print(blockchain.to_dict())

if __name__ == "__main__":
    main()
