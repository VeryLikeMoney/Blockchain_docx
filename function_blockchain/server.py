import requests
from flask import Flask, jsonify, request
from function_blockchain.blockchain import Blockchain
from function_blockchain.node import Node
from function_blockchain.transaction import Transaction
import json as _json
from function_blockchain.document import Document

app = Flask(__name__)

# Создаем экземпляр блокчейна
blockchain = Blockchain()
selfnode = None

def set_blockhain():
    return blockchain

# пример отправки файла по HTTP
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        pash =f"function_blockchain/{blockchain.whoami.port}/"+file.filename  # чтобы проверять на разных системах
        file.save(pash)
        file = Document(file.filename, blockchain.whoami)
        blockchain.whoami.add_mydocument(file) # напрямую добавлили файл для текущей ноды
        return 'File uploaded successfully.', 200
    else:
        return 'Upload failed.', 400

@app.route('/nodes/synch', methods=['POST'])
def synch_nodes():
    values = request.get_json()
    activ_document = values.get('activ_document')
    nodes = values.get('nodes') # list главной ноды
    chain = _json.loads(values.get('chain'))
    
    blockchain.activ_document = activ_document
    blockchain.add_nodes(nodes) #передача в функцию list где он добавляетсья в блокчейн к эксемпляры Node
    blockchain.inp_json(chain) # 
    return "OK", 200

@app.route('/nodes/main/connect', methods=['POST'])
def main_nodes():
    values = request.get_json()
    node = values.get('sender_nodes')
    blockchain.transaction.add_note(node) #cоздание транзакции по добавлению node в блокчейн
    blockchain.mine_block() # добыча блока 
    blockchain.out_json()
    blockchain.synchron() # функция которая рассылает main данные всем нодам ему известные
    return "OK", 200
    

@app.route('/connect', methods=['POST'])
def connect_node():
    "Первая функция для подключения ноды к блокчейну"
    values = request.get_json()
    main_node = values.get('main_node')
    if main_node is None:
        return "Error: Please supply a valid list of nodes", 400
    requests.post(f'http://{main_node}/nodes/main/connect', json={"sender_nodes": str(blockchain.whoami)})
    response = {
        "document": blockchain.activ_document,
        "nodes": blockchain.out_nodes()
    }
    return jsonify(response), 200
    

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': _json.loads(str(blockchain.chain)),
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

@app.route('/document/add', methods=['POST'])
def add_document():
    values = request.get_json()
    document = values.get('document')
    if not(document):
        return "Ошибка переданных данных о документе", 400
    blockchain.transaction.add_document(blockchain.whoami, document)
    return "OK", 200

@app.route('/document/delete', methods=['POST'])
def del_document():
    values = request.get_json()
    document = values.get('document')
    if not(document):
        return "Ошибка переданных данных о документе", 400
    blockchain.transaction.del_document(blockchain.whoami, document)
    response = {
        "document": blockchain.activ_document,
    }
    return jsonify(response), 200

@app.route('/document/sender', methods=['POST'])
def sender_document():
    values = request.get_json()
    filename = values.get("filename")
    recipient = values.get("recipient")

    blockchain.transaction.send_document(blockchain.whoami, recipient, filename)
    
    response = {
        "transaction": blockchain.transaction.loader()
    }
    return jsonify(response), 200
    

@app.route('/mine', methods=['GET'])
def mine_block():
    blockchain.mine_block()
    blockchain.synchron()
    response = {
            "document": blockchain.activ_document,
            "nodes": blockchain.out_nodes()
    }
    return jsonify(response), 200

@app.route('/document/activ', methods=['GET'])
def activ_docx():
    response = {
            "document": blockchain.activ_document,
            "nodes": blockchain.out_nodes()
    }
    return jsonify(response), 200

def start_server(ip:str, port:[str,int]):
    print("Сервер запущен")
    ip_port=ip+":"+port
    selfnode = Node(ip_port)
    blockchain.nodes.append(selfnode)
    blockchain.whoami = selfnode
    app.run(host=ip, port=int(port))
    


if __name__ == '__main__':
    from argparse import ArgumentParser
    
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    
    file_path = "123.docx"
    ip_port="127.0.0.1"+":"+str(port)
    selfnode = Node(ip_port)
    blockchain.nodes.append(selfnode)
    blockchain.whoami = selfnode
    if port == 5001:
        blockchain.transaction.add_document(selfnode, file_path)
        blockchain.mine_block()
    app.run(host='127.0.0.1', port=port)
    
