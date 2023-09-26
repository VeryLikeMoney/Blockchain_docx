from function_blockchain.node import Node
from function_blockchain.transaction import Transaction
from function_blockchain.block import Block
import json as _json
import requests
from function_blockchain.document import Document
import os

class Transaction_metod:
    
    def add_nodes(self, nodes:list):
        """Метод классов Blockchain(Transaction_metod)"""
        for node in nodes:
            if str(node) not in self.out_nodes():
                if str(self.whoami) != str(node):
                    self.nodes.append(Node(str(node)))
                else:
                    self.nodes.append(self.whoami)

    def add_document(self, info:dict):
        """Метод классов Blockchain(Transaction_metod)"""
        for key, val in info.items():
            for docx, hash in val:
                if key not in self.activ_document.keys():
                    self.activ_document[key] = {docx:hash}
                else:
                    self.activ_document[key][docx]=hash
            if key == str(self.whoami):
                val = list(tuple(el) for el in val)
                for docx,_ in val:
                    self.whoami.add_mydocument(Document(docx,owner=self.whoami))
    
    def del_document(self, info:dict):
        """Метод классов Blockchain(Transaction_metod)"""
        
        for key, val in info.items():
            print(val)       
            list_docx = self.activ_document.get(key)
            print(list_docx)
            for el in list_docx.copy().keys():
                if val in el:
                    list_docx.pop(el)
                    for docx in self.whoami.mydocument[:]:
                        if docx.fullname == el:
                            self.whoami.mydocument.remove(docx)
                            docx.del_docx() 
            if not list_docx:
                self.activ_document.pop(key)
            else:
                self.activ_document[key] = list_docx
    
    def send_document(self, info:list):
        # методы add и del уже будут в транзакции осталось обработать send 
        for transfer in info:
            sender = transfer.get('sender')
            recipient = transfer.get('recipient')
            filename = transfer.get('filename')
            filedocx = self.whoami.convertor(filename)      

            # как будто заработает 
            self.whoami.send_document(recipient, filedocx) # в чем суть  сначало файл отправляеться, там он себе в node добавяет новый файл
            info = {recipient: [(filedocx.fullname,filedocx.hash)]}
            self.add_document(info) # потом добавляет транзацкию адд для нового владельца(ноды), в обрабодчике он добавит в актив документы и все 
            info = {str(sender): filename}
            self.del_document(info) # потом удаляет документ как обычная транзакция
            # вопрос будет ли он продожать цикл обработичик - ответ она будет работь не так
                


class Blockchain(Transaction_metod):

    def __init__(self) -> None:
        """
        self.whoami – эксемпляр класса Node указывающий на текующую ноду 
        """
        self.chain = []
        self.nodes = []
        self.create_block = None
        self.whoami = None
        self.activ_document = {}
        self._transaction = None

    def new_block(self):
        if not self.chain:
            self.chain.append(Block(index=self.len))
        self.create_block = Block(index=self.len,previous_hash=self.last_block.hash)

    def complete_transaction(self):
        "Вызываются методы класса Transaction_metod"
        for key, val in  self._transaction.data.items():
            getattr(self,key,None)(val)

    def mine_block(self):
        """ 
            Метод для добычи блока в блокчейн 
            создаеться новый блок если он не был создан
            обрабатываеться транзакиця
            обновляется data в недобавленном блоке
            блок проходит proof и добавляетсья в блокчейн  
        """
        if self.create_block is None:
            self.new_block() # создание блока если его небыло
        self.complete_transaction() # обратотка транзакции
        self.create_block.data = self.transaction.loader()
        self.proof_of_work()
        self.chain.append(self.create_block)
        self.create_block, self._transaction = None, None

    @property
    def last_block(self):
        return self.chain[-1]

    @property
    def len(self):
        return len(self.chain)

    @staticmethod
    def valid_proof(block, proof:int):
        block.proof = proof
        res = block.get_hash()[:4] == "0000"
        if res:
            block.hash = block.get_hash()
        return res

    def proof_of_work(self):
        proof = 0
        while self.valid_proof(self.create_block, proof) is False:
            proof += 1
    
    def out_json(self) ->str:
        "Запись json файла с блокчейном"
        temp = str(self.whoami).split(':')
        filename = f"{temp[1]}.json"
        
        with open(filename, "w+") as json_file:
            blockchain_json = {}
            for block in self.chain:
                blockchain_json[block.index] = _json.loads(str(block))
            _json.dump(blockchain_json,json_file,indent=4)
            return  _json.dumps(blockchain_json)

    def inp_json(self, chain:dict):
        "Чтение json файла с блокчейном"
        self.chain = []
        temp = str(self.whoami).split(':')
        filename = f"{temp[1]}.json"
        
        with open(filename, "w") as json_file:
            blockchain_json = {}
            for key,block in chain.items():
                blockchain_json[key] = block
                self.chain.append(Block(*block.values()))
            _json.dump(blockchain_json,json_file,indent=4)
            
    def out_nodes(self):
        "Возвращает весь список Node со значениями type - str"
        return list(str(el) for el in self.nodes)

    def synchron(self):
        data = {
            "activ_document": self.activ_document,
            "nodes": self.out_nodes(),
            "chain": self.out_json()
        }
        for node in self.nodes:
            requests.post(f'http://{node}/nodes/synch', json=data)   
    
    @property
    def transaction(self)->Transaction:
        if not self._transaction:
            self._transaction = Transaction()
        return self._transaction


        

if __name__ == '__main__':     
    b1 = Blockchain()
    
    node_1 = Node('127.0.0.1:12345')
    node_2 = Node('127.0.0.1:12346')
    node_3 = Node('127.0.0.1:12347')
    node_4 = Node('127.0.0.1:12348')
    b1.whoami = node_3
    
    b1.transaction.add_note(node_1)
    b1.transaction.add_note(node_2)
    b1.mine_block()

    
    file_path = "123.docx"  # Укажите путь к вашему .docx файлу
    file_path1 = "1234.docx"  # Укажите путь к вашему .docx файлу
    b1.transaction.add_document(node_3, file_path)
    b1.transaction.add_document(node_3, file_path1)
    b1.transaction.add_note(node_4)
    b1.transaction.add_note(node_3)

    print(b1.transaction)

    b1.mine_block()
    
    print(b1.activ_document)
    print(b1.whoami.mydocument)

    """     
    for el in b1.chain:
    print(el)
    """
    """     
    for node in b1.nodes:
    print(node.mydocument)  
    """

    

    



