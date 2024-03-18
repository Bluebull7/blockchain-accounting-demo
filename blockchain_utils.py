import hashlib
import json 
import time

from blockchain import TransactionService, Blockchain


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

class RealTransactionService(TransactionService):
    
    def generate_transactions(self, num_transactions):
        return super().generate_transactions(num_transactions)

class RealBlockchain(Blockchain):
    # This is a real blockchain that uses the real transaction service 

    def add_block(self, block):
        super().add_block(block)
        return
    
    def remove_block(self, block):
        return super().remove_block(block)

    def get_block(self, index):
        return super().get_block(index)

    def get_all_blocks(self):
        return super().get_all_blocks()

    def get_latest_block(self):
        return super().get_latest_block()

    def get_size(self):
        return super().get_size()

    def is_valid(self):
        return super().is_valid()   

    def get_summary(self):
        return super().get_summary()
    
    def get_block_by_hash(self, block_hash):
        return super().get_block_by_hash(block_hash)

    def get_block_by_previous_hash(self, previous_hash):
        return super().get_block_by_previous_hash(previous_hash)

    def get_block_by_timestamp(self, timestamp):
        return super().get_block_by_timestamp(timestamp)

    def get_block_by_index(self, index):
        return super().get_block_by_index(index)

