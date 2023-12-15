from flask import Flask, jsonify, request, render_template
from blockchain import Blockchain
from penawaran import Penawaran
from permintaan import Permintaan
from transaksi import Transaksi
from datetime import datetime

app = Flask(__name__, template_folder='templates')
blockchain = Blockchain()

# Endpoint to get the entire blockchain
@app.route('/blockchain', methods=['GET'])
def get_blockchain():
    return jsonify(blockchain.blockchain_dict())

# Endpoint to view the entire blockchain
@app.route('/view_blockchain', methods=['GET'])
def view_blockchain_data_user_input():
    return jsonify(blockchain.to_dict())

# Endpoint to view the blockchain in a web page
@app.route('/view_blockchain_web', methods=['GET'])
def view_blockchain_web():
    return render_template('view_blockchain.html', blockchain=blockchain.blockchain_dict())

# Endpoint to add a new offer to the blockchain
@app.route('/penawaran', methods=['POST'])
def add_penawaran():
    try:
        penawaran_data = request.get_json()

        # Check if the received JSON data is valid for creating a Penawaran instance
        if not isinstance(penawaran_data, dict):
            raise ValueError("Data yang diberikan harus berupa objek penawaran")

        penawaran = Penawaran(**penawaran_data)
        blockchain.add_block(penawaran)
        return jsonify({"message": "Penawaran berhasil ditambahkan!"}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Endpoint to add an offer via user input
@app.route('/add_penawaran_user_input', methods=['GET', 'POST'])
def add_penawaran_user_input():
    if request.method == 'POST':
        try:
            # User input for Penawaran
            id_pelaku_usaha = request.form['id_pelaku_usaha']
            id_periode = request.form['id_periode']
            tanggal_penawaran = datetime.strptime(request.form['tanggal_penawaran'], "%Y-%m-%d").date()
            tanggal_awal_berlaku = datetime.strptime(request.form['tanggal_awal_berlaku'], "%Y-%m-%d").date()
            tanggal_akhir_berlaku = datetime.strptime(request.form['tanggal_akhir_berlaku'], "%Y-%m-%d").date()
            ptbae_ditawarkan = float(request.form['ptbae_ditawarkan'])
            satuan = request.form['satuan']
            harga = float(request.form['harga'])
            mata_uang = request.form['mata_uang']
            jumlah_terjual = float(request.form['jumlah_terjual'])
            satuan_terjual = request.form['satuan_terjual']
            sisa_penawaran = float(request.form['sisa_penawaran'])
            satuan_sisa_penawaran = request.form['satuan_sisa_penawaran']
            tanggal_terjual = datetime.strptime(request.form['tanggal_terjual'], "%Y-%m-%d").date()
            created_by = request.form['created_by']
            created_at = datetime.strptime(request.form['created_at'], "%Y-%m-%d %H:%M:%S")
            last_modified_by = request.form['last_modified_by']
            last_modified_at = datetime.strptime(request.form['last_modified_at'], "%Y-%m-%d %H:%M:%S")
            is_deleted = request.form['is_deleted']
            status = request.form['status']
            available_penawaran = float(request.form['available_penawaran'])
            is_spe = request.form['is_spe']

            penawaran = Penawaran(
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

            blockchain.add_block(penawaran)
            return jsonify({"message": "Penawaran berhasil ditambahkan!"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    else:
        # Render the form for GET requests
        return render_template('form_penawaran_user_input.html')
    
# Endpoint to view the entire blockchain
@app.route('/view_blockchain_data_all', methods=['GET'])
def view_blockchain_data_all():
    return jsonify(blockchain.to_dict())

@app.route('/add_transaksi_user_input', methods=['GET'])
def render_transaksi_form():
    # Render the form for GET requests
    return render_template('form_transaksi_user_input.html')

# Endpoint to add a new transaction via user input
@app.route('/add_transaksi_user_input', methods=['POST'])
def add_transaksi_user_input():
    try:
        # User input for Transaksi
        id_periode = request.form['id_periode']
        kode_transaksi = request.form['kode_transaksi']
        tanggal_transaksi_str = request.form['tanggal_transaksi']
        tanggal_transaksi = datetime.strptime(tanggal_transaksi_str, "%Y-%m-%d").date()
        id_pelaku_usaha = request.form['id_pelaku_usaha']
        beli_dari_pelaku_usaha = request.form['beli_dari_pelaku_usaha']
        jumlah_karbon_masuk = float(request.form['jumlah_karbon_masuk'])
        satuan_karbon_masuk = request.form['satuan_karbon_masuk']
        harga_beli = float(request.form['harga_beli'])
        nilai_beli_karbon = float(request.form['nilai_beli_karbon'])
        satuan_harga = request.form['satuan_harga']
        jual_ke = request.form['jual_ke']
        jumlah_karbon_keluar = float(request.form['jumlah_karbon_keluar'])
        satuan_karbon_keluar = request.form['satuan_karbon_keluar']
        harga_jual = float(request.form['harga_jual'])
        satuan_harga_jual = request.form['satuan_harga_jual']
        nilai_jual_karbon = float(request.form['nilai_jual_karbon'])
        token = request.form['token']
        saldo_emisi = float(request.form['saldo_emisi'])
        satuan_saldo = request.form['satuan_saldo']
        saldo_nilai_ekonomi = float(request.form['saldo_nilai_ekonomi'])
        satuan_mata_uang = request.form['satuan_mata_uang']
        token_expired = request.form['token_expired']
        approval_status = request.form['approval_status']
        approved_by = request.form['approved_by']
        approved_at_str = request.form['approved_at']
        approved_at = datetime.strptime(approved_at_str, "%Y-%m-%d %H:%M:%S")
        created_by = request.form['created_by']
        created_at_str = request.form['created_at']
        created_at = datetime.strptime(created_at_str, "%Y-%m-%d %H:%M:%S")
        modified_by = request.form['modified_by']
        is_deleted = request.form['is_deleted']
        file = request.form['file']
        id_penawaran = request.form['id_penawaran']
        id_permintaan = request.form['id_permintaan']
        id_transaksi_origin = request.form['id_transaksi_origin']
        is_spe = request.form['is_spe']
        is_direct_offset = request.form['is_direct_offset']

        transaksi = Transaksi(
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

        blockchain.add_block(transaksi)
        return jsonify({"message": "Transaksi berhasil ditambahkan!"}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/add_permintaan_user_input', methods=['GET', 'POST'])
def add_permintaan_user_input():
    if request.method == 'POST':
        try:
            permintaan_data = request.get.json()
            
            # User input for Permintaan
            id_pelaku_usaha = request.form['id_pelaku_usaha']
            id_periode = request.form['id_periode']
            tanggal_permintaan = datetime.strptime(request.form['tanggal_permintaan'], "%Y-%m-%d").date()
            tanggal_awal_berlaku = datetime.strptime(request.form['tanggal_awal_berlaku'], "%Y-%m-%d").date()
            tanggal_akhir_berlaku = datetime.strptime(request.form['tanggal_akhir_berlaku'], "%Y-%m-%d").date()
            ptbae_diminta = float(request.form['ptbae_diminta'])
            satuan = request.form['satuan']
            harga = float(request.form['harga'])
            mata_uang = request.form['mata_uang']
            jumlah_terbeli = float(request.form['jumlah_terbeli'])
            satuan_terbeli = request.form['satuan_terbeli']
            sisa_permintaan = float(request.form['sisa_permintaan'])
            satuan_sisa_permintaan = request.form['satuan_sisa_permintaan']
            tanggal_terbeli = datetime.strptime(request.form['tanggal_terbeli'], "%Y-%m-%d").date()
            created_by = request.form['created_by']
            created_at = datetime.strptime(request.form['created_at'], "%Y-%m-%d %H:%M:%S")
            last_modified_by = request.form['last_modified_by']
            last_modified_at = datetime.strptime(request.form['last_modified_at'], "%Y-%m-%d %H:%M:%S")
            is_deleted = request.form['is_deleted']
            status = request.form['status']
            available_permintaan = float(request.form['available_permintaan'])
            is_spe = request.form['is_spe']
            is_direct_offset = request.form['is_direct_offset']  # Add the missing parameter here

            permintaan = Permintaan(
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
                is_direct_offset=is_direct_offset
            )

            blockchain.add_block(permintaan)
            return jsonify({"message": "Permintaan berhasil ditambahkan!"}), 201
        except ValueError as ve:
            return jsonify({"error": str(ve)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
# Endpoint to render the form
@app.route('/form_penawaran_user_input', methods=['GET'])
def form_penawaran_user_input():
    return render_template('form_penawaran_user_input.html')

if __name__ == "__main__":
    app.run(debug=True)
