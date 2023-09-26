import hashlib as _hashlib
import datetime as _dt
import json as _json
from function_blockchain.transaction import Transaction

class Block:
 
    def __init__(self,index=None,timestamp=_dt.datetime.now(),data="0",proof=0,previous_hash="0",hash="0"*64):

        self._previous_hash = previous_hash 
        self._proof = proof
        self._index = index
        self._data = data
        self._timestamp = timestamp
        self._hash = hash 
    
    def get_hash(self):
        header_bin = (str(self._previous_hash) +
                      str(self._data) +
                      str(self._timestamp)+
                      str(self._proof)+
                      str(self._index))

        inner_hash = _hashlib.sha256(header_bin.encode()).hexdigest().encode()
        outer_hash = _hashlib.sha256(inner_hash).hexdigest()
        return outer_hash
    
    @property
    def hash(self):
        return self._hash

    @hash.setter
    def hash(self, new_hash):
        self._hash = new_hash

    @property
    def proof(self):
        return self._proof

    @proof.setter
    def proof(self, new_proof:int):
        self._proof = new_proof

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data:Transaction):
        self._data = new_data

    @property
    def index(self):
        return self._index


    def __repr__(self):
        return self.block_json()
    
    def __str__(self):
        return self.block_json()

    def block_json(self):
        block = {
            "index": self._index,
            "timestamp": str(self._timestamp),
            "transactions": self._data,
            "proof": self._proof,
            "previous_hash": self._previous_hash,
            "hash": self._hash
        }
        block = _json.dumps(block, default= lambda obj: str(obj))
        block = _json.loads(block)
        return str(block).replace("'", '"')


if __name__ == "__main__":
    block0 = Block()
    print(block0)
    block1 = Block(1,1, block0.hash)
    print(block1)