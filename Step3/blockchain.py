import datetime as date
import hashlib
import json
import os
from .block import *

class BlockChain:
    def __init__(self):
        self.blocks = []
        self.load_blocks('data')
        if len(self.blocks)==0:
            genesis_block = create_genesis_block()
            genesis_block.proof_of_work()
            genesis_block.save('data')
            self.blocks.append(genesis_block)

    def add_block(self,data):
        previous_hash = self.blocks[-1].hash
        previous_index = self.blocks[-1].index
        new_block = Block(data=data,previous_hash = previous_hash,index = previous_index+1)
        new_block.proof_of_work()
        new_block.save('data')
        self.blocks.append(new_block)

    def load_blocks(self,datadir):
        if not os.path.exists(datadir):
            os.mkdir(datadir)
        for filename in os.listdir(datadir):
            jsonfile = '%s/%s' % (datadir, filename)
            print(jsonfile)
            with open(jsonfile, 'r') as block_file:
                info = json.load(block_file)
                print(info)
                bk = Block(index = int(info['index']),
                           timestamp=info['timestamp'],
                           previous_hash =  info['prev_hash'],
                           hash=info['hash'] ,
                           data = info['data'],
                           nonce =int(info['nonce']) )
                self.blocks.append(bk)

    def print_chain(self):
        for bk in self.blocks:
            print("*******" *10)
            print("Block Index: %d" % bk.index)
            print("Prev. hash: %s" % bk.previous_hash)
            print("Data: %s" % bk.data)
            print("Nonce: %s" % bk.nonce)
            print("Hash: %s" % bk.hash)

