from datetime import datetime

from block import Block


class TestBasic(object):
    def test_create_genesis_block(self):
        genesis_block = make_genesis_block()
        assert genesis_block.index is 0
        assert genesis_block.timestamp < datetime.now()
        assert genesis_block.data.get('proof-of-work', None) is 1
        assert genesis_block.data.get('transactions', None) == []
        assert genesis_block.previous_hash is '0'


# helper functions
def make_genesis_block():
    return Block.create_genesis_block()