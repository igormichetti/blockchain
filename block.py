import time
import hashlib
from contract import Transaction

contract = Transaction('Sender Public Key' , 'Sender Private Key', 'Recipient Public Key','Amount to Send')

class Block():
    def __init__(self, data, previous_hash, timestamp):
        self.hash = hashlib.sha256()
        self.previous_hash = previous_hash
        self.nonce = 0
        self.data = contract.sign_transaction()
        self.timestamp = time.time()
        
    def mine(self, difficulty):
        self.hash.update(str(self).encode('utf-8'))
        while int(self.hash.hexdigest(), 16) > 2**(256-difficulty):
            self.nonce += 1
            self.hash = hashlib.sha256()
            self.hash.update(str(self).encode('utf-8'))
        
    def __str__(self):
        return f"{self.previous_hash.hexdigest()}{self.data}{self.nonce}{self.timestamp}"
