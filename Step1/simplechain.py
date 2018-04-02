from Step1.blockchain import BlockChain

if __name__ == '__main__':
    blockchain = BlockChain()
    blockchain.add_block("Send 1 BTC to Guoyunli")
    blockchain.add_block("Send 2 more BTC to Guoyunli")
    blockchain.print_chain()


