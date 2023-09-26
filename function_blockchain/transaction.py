import json as _json
from function_blockchain.node import Node
from function_blockchain.document import Document

class Transaction:

    def __init__(self) -> None:
        self.data = {}
    
    def add_note(self, node:Node):
        """Метод класса Transaction"""
        if "add_nodes" not in self.data.keys():
            self.data["add_nodes"] = [node]
        else:
            self.data["add_nodes"].append(node)

    def add_document(self, node:Node, filename:str):
        """Метод класса Transaction"""
        file = Document(filename, node)
        # если нет файла что тогда? @22
        if file.calculate_file_hash(): 
            if "add_document" not in self.data.keys():
                self.data["add_document"] ={str(node):[(file.fullname,file.hash)]}
            else:
                self.data["add_document"][str(node)].append((file.fullname,file.hash))
    
    def del_document(self, node:Node, filename:str):
        """Метод класса Transaction"""
        if filename in node.listdocument:
            for docx in node.mydocument[:]:
                if docx.fullname == filename:
                    if "del_document" not in self.data.keys():
                        self.data["del_document"] = {str(node): docx.fullname}  # надобы исправить              
                    else:
                        self.data["del_document"][str(node)] = docx.fullname
                    return True
        return False   
        
    def send_document(self,sender:Node,recipient:str,filename:str):
        """Метод класса Transaction"""
        # НЕ проверена
        filedocx = sender.convertor(filename)
        if filedocx:
            if "send_document" not in self.data.keys():
                self.data["send_document"] = [{"sender": sender,
                                            "recipient": recipient,
                                            "filename": filename,
                                            "hashdocx": filedocx.hash}]                 
            else:
                d = {"sender": sender,
                    "recipient": recipient,
                    "filename": filename,
                    "hashdocx": filedocx.hash}
                self.data["send_document"].append(d) 

    def __repr__(self) -> str:
        return self.printer()
    
    def __str__(self) -> str:
        return self.printer()

    def loader(self)-> dict:
        trs = _json.dumps(self.data, default= lambda node: str(node))
        return _json.loads(trs)

    def printer(self)-> str:
        return str(self.loader()).replace("'", '"')
    

    

if __name__ == '__main__':
    node_1 = Node('127.0.0.1','12345','Node1')
    node_2 = Node('127.0.0.1','12346','Node2')
    trs = Transaction()
    trs.add_note(node_1.ip_port)
    trs.add_note(node_2)
    print(type(trs.loader()))