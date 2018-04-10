from .blockchain import BlockChain
from optparse import OptionParser
def get_paras():
    try:
        opt = OptionParser(usage="usage: SimpleChain [optinos]")
        opt.add_option("-a", "--addblock",
                       action="store_true",
                       dest="addblock",
                       default=False,
                       help="Add Block")
        opt.add_option("-p", "--printchain",
                       action="store_true",
                       dest="printchain",
                       default=False,
                       help="Print Chain")
        opt.add_option("-d", "--data",
                       action="store",
                       type='string',
                       dest="data",
                       default=None,
                       help="Specify the block data")
        (options, args) = opt.parse_args()
        print(options)
        print(args)
        return options
    except Exception as ex:
        print("exception :{0}".format(str(ex)))
        return None

if __name__ == '__main__':
    options = get_paras()
    print(options)
    blockchain = BlockChain()
    if options.printchain == True:
        blockchain.print_chain()
    if options.addblock and options.data is not None:
        blockchain.add_block(options.data)


