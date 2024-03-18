from abc import ABC, abstractmethod

class Block(ABC):
    def __init__(self, timestamp, summary, block_hash, previous_hash):
        self.timestamp = timestamp
        self.summary = summary
        self.block_hash = block_hash
        self.previous_hash = previous_hash

    
class Blockchain(ABC):
    @abstractmethod
    def add_block(self, block):
        pass

    @abstractmethod
    def remove_block(self, block):
        pass

    @abstractmethod
    def get_block(self, index):
        pass

    @abstractmethod
    def get_all_blocks(self):
        pass

    @abstractmethod
    def get_latest_block(self):
        pass

    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def is_valid(self):
        pass

    @abstractmethod
    def get_summary(self):
        pass

    @abstractmethod
    def get_block_by_hash(self, block_hash):
        pass

    @abstractmethod
    def get_block_by_previous_hash(self, previous_hash):
        pass

    @abstractmethod
    def get_block_by_timestamp(self, timestamp):
        pass

    @abstractmethod
    def get_block_by_index(self, index):
        pass

class TransactionService(ABC):
    @abstractmethod
    def generate_transactions(self, num_transactions):
        pass
