import hashlib as _hashlib
import os
import requests

class Document:

    def __init__(self, fullname:str, owner:str) -> None:
        fullname = fullname.split('.')
        self.extension = fullname[-1]
        self.name = ''.join(str(x) for x in fullname[:-1])
        self.owner = owner
        self.path = f"function_blockchain/{self.owner.port}/{self.fullname}"

    @property
    def fullname(self):
        return self.name +"."+ self.extension
    
    @property
    def hash(self):
        return self.calculate_file_hash()

    def document_full(self, url):
        with open(self.path, 'rb') as file:
            files = {'file': (self.fullname, file)}
            response = requests.post(url, files=files)
        return  response.status_code 

    def del_docx(self) -> None:
        os.remove(self.path)

    def __str__(self)->str:
        return self.fullname +' hash:' + self.hash
    
    def __repr__(self)->str:
        return self.fullname +' hash:' + self.hash
    
    def calculate_file_hash(self)->str:
        hash_obj = _hashlib.new("sha256")
        try:
            with open(self.path, "rb") as file:
                while chunk := file.read(8192):  # Read the file in 8KB chunks
                    hash_obj.update(chunk)
        except Exception as e:
            print(e)
            return None
        return hash_obj.hexdigest()
    
    def fullname_hash(self)->dict:
        return {
            self.fullname: self.hash
        }