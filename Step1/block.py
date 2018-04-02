import datetime as date
import hashlib
import json

class Block:
    def __init__(self,data,previous_hash=''):
        self.timestamp =  str(date.datetime.now())
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.create_hash()

    def create_hash(self):
        block_header = dict(timestamp=self.timestamp,
                          data=self.data,
                          previous_hash=self.previous_hash)
        block_string = json.dumps(block_header, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

def create_genesis_block():
    #No previous hash
    return Block(data ='First block data')