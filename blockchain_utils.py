import hashlib
import json 
import time 

class Block:
    def __init__(self, summary, previous_hash, timestamp, block_hash):
        self.summary = summary
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.block_hash = block_hash


class BlockchainUtils:
    @staticmethod
    def calculate_block_hash(block_data, previous_hash):
        block_strings = json.dumps(block_data, sort_keys=True).encode()
        previous_hash_of_string = previous_hash.encode()
        combined_hash = hashlib.sha256(block_strings + previous_hash_of_string).hexdigest()

        return combined_hash


