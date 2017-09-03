import json
import requests

from flask import Flask, request
from block import Block


node = Flask(__name__)
blockchain = [Block.create_genesis_block()]
node_transactions = []
miner_address = '12345'


@node.route('/transaction', methods=['POST'])
def write_transaction():
    if request.method == 'POST':
        transaction = request.get_json()
        node_transactions.append(transaction)
        print "New transaction"
        print "FROM: {}".format(transaction['from'])
        print "TO: {}".format(transaction['to'])
        print "AMOUNT: {}\n".format(transaction['amount'])
        return "Transaction successful\n"


def proof_of_work(last_proof):
    inc = last_proof + 1
    while not (inc % 9 == 0 and inc % last_proof == 0):
        inc += 1
    return inc


@node.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain[-1]
    last_proof = last_block.data['proof-of-work']
    proof = proof_of_work(last_proof)

    # Reward
    node_transactions.append(
        {'from': 'network', 'to': miner_address, 'amount': 1}
    )

    new_block_data = {
        'proof-of-work': proof,
        'transactions': node_transactions[:]
    }
    new_block = Block.next_block(last_block, new_block_data)
    blockchain.append(new_block)
    node_transactions[:] = []

    return new_block.to_json() + '\n'


@node.route('/blocks', methods=['GET'])
def get_blocks():
    return json.dumps(map(lambda x: x.to_json(), blockchain))


def find_new_chains():
    other_chains = []
    for node_url in peer_nodes:
        chain = requests.get(node_url + '/blocks').content
        chain = json.loads(chain)
        other_chains.append(chain)
    return other_chains


def consensus():
    other_chains = find_new_chains()
    longest_chain = blockchain
    for chain in other_chains:
        if len(chain) > len(longest_chain):
            longest_chain = chain

    blockchain = longest_chain

