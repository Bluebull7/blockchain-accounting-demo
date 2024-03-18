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

