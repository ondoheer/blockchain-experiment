import hashlib
import json
from time import time

class Blockchain(object):
    """
    Responsible for managing the chain,
    stores transactions and adds new blocks to the chain
    """

    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # create the genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Creates a new block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time(),
            "transactions": self.current_transactions,
            "proof": proof,
            "previous_hash": previous_hash or self.hash(self.chain[-1])
        }

        # reset current list of transactions

        self.current_transactions = []
        
        self.chain.append(block)
        return block
        

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction that will go into the newxt mined block
        adds a transaction to the list, 
        it returns the index of the block which the transaction 
        will be added to—the next one to be mined
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """
        self.current_transactions.append({
            "sender":sender,
            "recipient":recipient,
            "amount":amount
        })
        return self.last_block["index"] + 1

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

