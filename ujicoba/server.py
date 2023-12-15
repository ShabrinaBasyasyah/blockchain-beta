from datetime import datetime
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from blockchain import Blockchain
from penawaran import Penawaran
from permintaan import Permintaan
from transaksi import Transaksi

app = Flask(__name__)
api = Api(app)

class BlockResource(Resource):
    def get(self):
        return jsonify(blockchain.blocks)

api.add_resource(BlockResource, '/blocks')

class AddBlockResource(Resource):
    def post(self):
        try:
            data = request.get_json()
            block_type = data.get('type')

            if block_type not in ['penawaran', 'transaksi', 'permintaan']:
                raise ValueError("Type must be 'penawaran', 'transaksi', or 'permintaan'.")

            block_data = data.get('data')
            if block_type == 'penawaran':
                block_instance = Penawaran(**block_data)
            elif block_type == 'transaksi':
                block_instance = Transaksi(**block_data)
            elif block_type == 'permintaan':
                block_instance = Permintaan(**block_data)
            else:
                raise ValueError("Invalid block type.")

            blockchain.add_block(block_instance.to_dict())
            return {"message": f"{block_type.capitalize()} added successfully."}, 201
        except Exception as e:
            return {"error": str(e)}, 400

api.add_resource(AddBlockResource, '/add_block')

class BlockchainInfoResource(Resource):
    def get(self):
        return {"total_emissions": blockchain.calculate_total_emissions()}

api.add_resource(BlockchainInfoResource, '/blockchain_info')

if __name__ == '__main__':
    blockchain = Blockchain()
    app.run(debug=True)
