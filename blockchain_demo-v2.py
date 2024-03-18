import hashlib
import json

# Function to generate random transactions

def generate_transaction_data(num_transactions):
    transactions = []
    for i in range(num_transactions):
        transaction = {
            'sender': f"User_{i+1}",
            'receiver': f"User_{random.randint(1, num_transactions)}",
            'amount': random.randint(1, 100)
        }
        transactions.append(transaction)
    return transactions

# Function to summarize the block
def summarize_block(block):
    return {
        'index': block['index'],
        'timestamp': block['timestamp'],
        'previous_hash': block['previous_hash'],
        'transactions': block['transactions'],
        'hash': block['hash']
    }

class Blockchain:
    def __init__(self):
        self.chain = [create_genesis_block()]

    def add_block(self, transactions):
        self.chain.append(create_block(transactions, self.chain[-1]))

    def print_blockchain(self):
        for block in self.chain:
            print(json.dumps(summarize_block(block), indent=2))

    def validate_blockchain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block['hash'] != calculate_block_hash(current_block, previous_block['hash']):
                return False
        return True

# Function to calculate the hash of the block using SHA-256
def calculate_block_hash(block_data, previous_hash):
    data_string = json.dumps(block_data, sort_keys=True).encode()
    combined_hash = hashlib.sha256(data_string + previous_hash.encode()).hexdigest()

    return combined_hash

def create_genesis_block():
    return {
        'index': 0,
        'timestamp': 0,
        'previous_hash': "0",
        'transactions': [],
        'hash': "0"
    }

def create_block(transactions, previous_hash):
    block = {
        'index': previous_hash['index'] + 1,
        'timestamp': time.time(),
        'previous_hash': previous_hash['hash'],
        'transactions': transactions,
        'hash': ""
    }
    block['hash'] = calculate_block_hash(block, previous_hash['hash'])
    return block


