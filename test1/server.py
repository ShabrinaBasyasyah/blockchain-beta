import socket
import json
import logging
from blockchain import Blockchain
from penawaran import Penawaran
from permintaan import Permintaan
from transaksi import Transaksi

# Membuat instansiasi blockchain di luar fungsi
blockchain = Blockchain()

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        try:
            request = json.loads(data.decode())
            logging.info("Received request from client: %s", request)
            
            if request["method"] == "get_blockchain":
                response = json.dumps({
                    "blocks": [block.to_dict() for block in blockchain.blocks],
                    "total_emissions": blockchain.calculate_total_emissions(),
                }, indent=4)
            elif request["method"] == "add_block":
                if isinstance(request["data"], Permintaan) or isinstance(request["data"], Penawaran) or isinstance(request["data"], Transaksi):
                    blockchain.add_block(request["data"])
                    response = json.dumps({"status": "success"})
                else:
                    response = json.dumps({"status": "failed"})
            else:
                response = json.dumps({"status": "failed"})

            logging.info("Sending response to client:\n%s", response)
            client_socket.sendall(response.encode())

        except json.JSONDecodeError:
            logging.error("Failed to decode JSON.")
            response = json.dumps({"status": "failed"})
            client_socket.sendall(response.encode())
            break

        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            response = json.dumps({"status": "failed"})
            client_socket.sendall(response.encode())
            break

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8000))
    server_socket.listen(1)

    print("Server is running on port 8000...")

    while True:
        client_socket, _ = server_socket.accept()
        print("Client connected...")
        handle_client(client_socket)
        client_socket.close()
        print("Client disconnected...")

if __name__ == "__main__":
    main()
