import hashlib
import json

class User:
    def __init__(self, id_pelaku_usaha, nama, beli_dari_pelaku_usaha, id_pelaku_usaha_penawaran):
        # Initialize the attributes of the user
        self.id_pelaku_usaha = id_pelaku_usaha
        self.nama = nama
        self.beli_dari_pelaku_usaha = beli_dari_pelaku_usaha
        self.id_pelaku_usaha_penawaran = id_pelaku_usaha_penawaran

    def __repr__(self):
        return f"User(id_pelaku_usaha={self.id_pelaku_usaha}, nama={self.nama}, beli_dari_pelaku_usaha={self.beli_dari_pelaku_usaha}, id_pelaku_usaha_penawaran={self.id_pelaku_usaha_penawaran})"
