import hashlib
import json
import time

class Blockchain:
    @staticmethod
    def calculate_hash(index, previous_hash, timestamp, data):
        value = f"{index}{previous_hash}{timestamp}{json.dumps(data)}"
        return hashlib.sha256(value.encode()).hexdigest()

    @classmethod
    def create_block(cls, index, previous_hash, data):
        timestamp = time.time()
        block_hash = cls.calculate_hash(index, previous_hash, timestamp, data)
        return {
            "index": index,
            "timestamp": timestamp,
            "data": data,
            "previous_hash": previous_hash,
            "hash": block_hash
        }