import requests
from function_blockchain.document import Document 

class Node:
    def __init__(self, ip4_port:str) -> None:
        """ ip4_port -строка типа ip:port"""
        ip4_port = ip4_port.split(':')
        self.__ip4 = ip4_port[0]
        self.__port = ip4_port[1]
        self.mydocument = []

    def add_mydocument(self, document:Document):
        """ Добавляет файл в список доступных документов для этой ноды"""
        if document.fullname not in list(el.fullname for el in self.mydocument):
            self.mydocument.append(document)

    def send_document(self, recipient, document:Document)->bool:
        """ Отправляет файл по HTTP """
        url = f'http://{str(recipient)}/upload'
        response = document.document_full(url)
        if response == 200:
            return True
        else:
            return False

    def convertor(self, filename:str)->Document:
        """ Преобразует str в Document """
        for docx in self.mydocument:
            if docx.fullname == filename:
                return docx

    @property
    def listdocument(self):
        return list(el.fullname for el in self.mydocument)

    @property
    def ip_port(self):
        return self.__ip4 +':'+self.__port
    
    @property
    def port(self):
        return self.__port
  
    def __repr__(self) -> str:
        return self.ip_port

    def __str__(self) -> str:
        return self.ip_port

def main():
    url = 'http://127.0.0.1:80/upload'  # Замените на ваш адрес сервера
    filename = '123.docx'
    
    with open(filename, 'rb') as file:
        files = {'file': (filename,file)}
        response = requests.post(url, files=files)
        
    if response.status_code == 200:
        print("File uploaded successfully.")
    else:
        print("Upload failed.")

if __name__ == '__main__':
    node_1 = Node('127.0.0.1', '12345')
    file_path = "123.docx"  # Укажите путь к вашему .docx файлу
    file_path1 = "1234.docx"  # Укажите путь к вашему .docx файлу
    node_1.add_document(file_path)
    node_1.add_document(file_path1)
    print(node_1)