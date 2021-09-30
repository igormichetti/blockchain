from chain import Chain
from contract import Transaction

contract = Transaction('Sender Public Key' , 'Sender Private Key', 'Recipient Public Key','Amount to Send')

chain = Chain(20)

i = 0

if __name__ == '__main__':
    
    while(True):
        data = contract.sign_transaction()
        chain.add_to_pool(data)
        chain.mine()
        print(chain.blocks[-1])
        



