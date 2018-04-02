import datetime as date
import hashlib
import json
import os
from .block import *

class BlockChain:
    def __init__(self):
        self.blocks = []
        genesis_block = create_genesis_block()
        self.blocks.append(genesis_block)

    def add_block(self,data):
        previous_hash = self.blocks[-1].hash
        self.blocks.append(Block(data=data,previous_hash = previous_hash))

    def print_chain(self):
        count = 1
        for bk in self.blocks:
            print("*******" *10)
            print("Block number: %d" % count)
            print("Prev. hash: %s" % bk.previous_hash)
            print("Data: %s" % bk.data)
            print("Hash: %s" % bk.hash)
            count += 1
