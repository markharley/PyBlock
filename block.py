import hashlib
import json

from datetime import datetime
from merkle import compute_merkle


class Block(object):

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.merkle_root = compute_merkle(self.data['transactions'])
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(str(self.index) +
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash) +
                   str(self.merkle_root))
        return sha.hexdigest()

    def to_json(self):
        return json.dumps({
            'index': self.index,
            'timestamp': str(self.timestamp),
            'data': self.data,
            'hash': self.hash,
            'merkle': self.merkle_root,
        })

    @classmethod
    def create_genesis_block(cls):
        genesis_data = {
            'proof-of-work': 1,
            'transactions': [],
        }
        return cls(0, datetime.now(), genesis_data, '0')

    @classmethod
    def next_block(cls, previous_block, data):
        index = previous_block.index + 1
        timestamp = datetime.now()
        return cls(index, timestamp, data, previous_block.hash)


if __name__ == '__main__':

    blockchain = [Block.create_genesis_block()]
    previous_block = blockchain[0]

    for i in range(20):
        data = 'This is block {}'.format(previous_block.index + 1)
        next_block = Block.next_block(previous_block, data)
        previous_block = next_block
        print "New block index {} has been added to the blockchain".format(next_block.index)
        print "json: {}".format(next_block.to_json())

