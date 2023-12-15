import hashlib
import json
from datetime import datetime

class Permintaan:
    def __init__(self, id, id_pelaku_usaha, tanggal_permintaan, ptbae_diminta, satuan, harga, **kwargs):
        self.id = id
        self.id_pelaku_usaha = id_pelaku_usaha
        self.tanggal_permintaan = tanggal_permintaan
        self.ptbae_diminta = ptbae_diminta
        self.satuan = satuan
        self.harga = harga
        self.additional_data = kwargs

    def to_dict(self):
        return {
            "id": self.id,
            "id_pelaku_usaha": self.id_pelaku_usaha,
            "tanggal_permintaan": self.tanggal_permintaan,
            "ptbae_diminta": self.ptbae_diminta,
            "satuan": self.satuan,
            "harga": self.harga,
            **self.additional_data
        }

class Penawaran:
    def __init__(self, id, id_pelaku_usaha, tanggal_penawaran, ptbae_ditawarkan, satuan, harga, **kwargs):
        self.id = id
        self.id_pelaku_usaha = id_pelaku_usaha
        self.tanggal_penawaran = tanggal_penawaran
        self.ptbae_ditawarkan = ptbae_ditawarkan
        self.satuan = satuan
        self.harga = harga
        self.additional_data = kwargs

    def to_dict(self):
        return {
            "id": self.id,
            "id_pelaku_usaha": self.id_pelaku_usaha,
            "tanggal_penawaran": self.tanggal_penawaran,
            "ptbae_ditawarkan": self.ptbae_ditawarkan,
            "satuan": self.satuan,
            "harga": self.harga,
            **self.additional_data
        }

class Transaksi:
    def __init__(self, id, id_periode, kode_transaksi, tanggal_transaksi, jumlah_karbon_masuk, satuan_karbon_masuk,
                 harga_beli, nilai_beli_karbon, **kwargs):
        self.id = id
        self.id_periode = id_periode
        self.kode_transaksi = kode_transaksi
        self.tanggal_transaksi = tanggal_transaksi
        self.jumlah_karbon_masuk = jumlah_karbon_masuk
        self.satuan_karbon_masuk = satuan_karbon_masuk
        self.harga_beli = harga_beli
        self.nilai_beli_karbon = nilai_beli_karbon
        self.additional_data = kwargs

    def to_dict(self):
        return {
            "id": self.id,
            "id_periode": self.id_periode,
            "kode_transaksi": self.kode_transaksi,
            "tanggal_transaksi": self.tanggal_transaksi,
            "jumlah_karbon_masuk": self.jumlah_karbon_masuk,
            "satuan_karbon_masuk": self.satuan_karbon_masuk,
            "harga_beli": self.harga_beli,
            "nilai_beli_karbon": self.nilai_beli_karbon,
            **self.additional_data
        }

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

    # Meminta pengguna untuk memasukkan data permintaan
    print("Masukkan data permintaan:")
    id_permintaan = int(input("ID Permintaan: "))
    id_pelaku_usaha = int(input("ID Pelaku Usaha: "))
    tanggal_permintaan = input("Tanggal Permintaan: ")
    ptbae_diminta = float(input("PTBAE Diminta: "))
    satuan_permintaan = input("Satuan Permintaan: ")
    harga_permintaan = float(input("Harga Permintaan: "))

    # Membuat objek Permintaan berdasarkan input pengguna
    permintaan = Permintaan(
        id=id_permintaan,
        id_pelaku_usaha=id_pelaku_usaha,
        tanggal_permintaan=tanggal_permintaan,
        ptbae_diminta=ptbae_diminta,
        satuan=satuan_permintaan,
        harga=harga_permintaan
    )

    # Menambahkan blok baru dengan data permintaan
    blockchain.add_block(permintaan)

    # Meminta pengguna untuk memasukkan data penawaran
    print("\nMasukkan data penawaran:")
    id_penawaran = int(input("ID Penawaran: "))
    id_pelaku_usaha_penawaran = int(input("ID Pelaku Usaha Penawaran: "))
    tanggal_penawaran = input("Tanggal Penawaran: ")
    ptbae_ditawarkan = float(input("PTBAE Ditawarkan: "))
    satuan_penawaran = input("Satuan Penawaran: ")
    harga_penawaran = float(input("Harga Penawaran: "))

    # Membuat objek Penawaran berdasarkan input pengguna
    penawaran = Penawaran(
        id=id_penawaran,
        id_pelaku_usaha=id_pelaku_usaha_penawaran,
        tanggal_penawaran=tanggal_penawaran,
        ptbae_ditawarkan=ptbae_ditawarkan,
        satuan=satuan_penawaran,
        harga=harga_penawaran
    )

    # Menambahkan blok baru dengan data penawaran
    blockchain.add_block(penawaran)

    # Meminta pengguna untuk memasukkan data transaksi
    print("\nMasukkan data transaksi:")
    id_transaksi = int(input("ID Transaksi: "))
    id_periode = int(input("ID Periode: "))
    kode_transaksi = input("Kode Transaksi: ")
    tanggal_transaksi = input("Tanggal Transaksi: ")
    jumlah_karbon_masuk = float(input("Jumlah Karbon Masuk: "))
    satuan_karbon_masuk = input("Satuan Karbon Masuk: ")
    harga_beli = float(input("Harga Beli: "))
    nilai_beli_karbon = float(input("Nilai Beli Karbon: "))

    # Membuat objek Transaksi berdasarkan input pengguna
    transaksi = Transaksi(
        id=id_transaksi,
        id_periode=id_periode,
        kode_transaksi=kode_transaksi,
        tanggal_transaksi=tanggal_transaksi,
        jumlah_karbon_masuk=jumlah_karbon_masuk,
        satuan_karbon_masuk=satuan_karbon_masuk,
        harga_beli=harga_beli,
        nilai_beli_karbon=nilai_beli_karbon
    )

    # Menambahkan blok baru dengan data transaksi
    blockchain.add_transaksi(transaksi)

    # Cetak blockchain
    print("\nBlockchain:")
    print(blockchain.to_dict())

if __name__ == "__main__":
    main()
