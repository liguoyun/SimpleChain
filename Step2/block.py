import datetime as date
import hashlib
import json

NUM_ZEROS = 3

class Block:
    def __init__(self,data,previous_hash=''):
        self.timestamp =  str(date.datetime.now())
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        #self.hash = self.create_hash()

    def proof_of_work(self):
        nonce = 0
        block_hash = create_hash(nonce,self.timestamp,self.data,self.previous_hash)
        print("minning: nonce = %d  block_hash = %s" %(nonce,block_hash))
        while str(block_hash[0:NUM_ZEROS]) != '0' * NUM_ZEROS:
            nonce += 1
            block_hash = create_hash(nonce, self.timestamp, self.data, self.previous_hash)
            print("minning: nonce = %d  block_hash = %s" % (nonce, block_hash))

        print("minning done")
        self.nonce = nonce
        self.hash = block_hash

def create_hash(nonce,timestamp,data,previous_hash):
    block_header = dict(timestamp=timestamp,
                    data=data,
                    previous_hash=previous_hash,
                    nonce =nonce )
    block_string = json.dumps(block_header, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

def create_genesis_block():
    #No previous hash
    return Block(data ='First block data')