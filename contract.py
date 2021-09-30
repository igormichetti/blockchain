from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5  
from Crypto.Hash import SHA
import binascii
from collections import OrderedDict


class Transaction:

    def __init__(self, sender_public_key, sender_private_key, recipient_public_key, amount):
        self.sender_public_key = sender_public_key
        self.sender_private_key = sender_private_key
        self.recipient_public_key = recipient_public_key
        self.amount = amount
    
    def to_dict(self):
        return OrderedDict({
            'sender_public_key': self.sender_public_key,
            'recipient_public_key': self.recipient_public_key,
            'amount': self.amount,
        })

    def sign_transaction(self):
        RSA.importKey(externKey, passphrase=None)
        private_key = RSA.import_key(binascii.unhexlify(self.sender_private_key))
        # Use RSA.importKey para importar a chave.
        signer = PKCS1_v1_5.new(private_key)  # Create a signature using sender_private_key using a PKCS algorithm
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        
        return binascii.hexlify(signer.sign(h)).decode('ascii')
        