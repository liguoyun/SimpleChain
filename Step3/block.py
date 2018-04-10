import datetime as date
import hashlib
import json
import os
import sys
NUM_ZEROS = 5

class Block:
    def __init__(self,data,timestamp = None,index=0,nonce = 0,previous_hash='',hash = ''):
        if timestamp is None:
            self.timestamp =  str(date.datetime.now())
        else:
            self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = hash
        self.nonce = nonce
        self.index = index
        #self.hash = self.create_hash()

    def __dict__(self):
        info = {}
        info['index'] = str(self.index)
        info['timestamp'] = str(self.timestamp)
        info['prev_hash'] = str(self.previous_hash)
        info['hash'] = str(self.hash)
        info['data'] = str(self.data)
        info['nonce'] = str(self.nonce)
        return info

    def proof_of_work(self):
        nonce = 0
        block_hash = create_hash(nonce,self.timestamp,self.data,self.previous_hash)
        #print("minning: nonce = %d  block_hash = %s" %(nonce,block_hash))
        while str(block_hash[0:NUM_ZEROS]) != '0' * NUM_ZEROS:
            nonce += 1
            block_hash = create_hash(nonce, self.timestamp, self.data, self.previous_hash)
            #print("minning: nonce = %d  block_hash = %s" % (nonce, block_hash))
        print("minning done")
        self.nonce = nonce
        self.hash = block_hash

    def save(self,datadir):
        index_string = str(self.index).zfill(6)  # front of zeros so they stay in numerical order
        filename = '%s/%s.json' % (datadir, index_string)
        if not os.path.exists(datadir):
            os.mkdir(datadir)
        with open(filename, 'w') as block_file:
            json.dump(self.__dict__(), block_file)

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