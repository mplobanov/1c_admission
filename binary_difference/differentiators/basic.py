class BasicDifferentiator:
    def __init__(self, batch_size: int):
        self.batch_size = 1024
        pass

    # makes part of diff file
    def make_diff_batch(self, old_batch: bytes, new_batch: bytes) -> bytes:
        assert len(old_batch) == self.batch_size == len(new_batch)
        return bytes(0)

    def get_recovered_batch(self, old_batch: bytes, diff_batch: bytes) -> bytes:
        assert len(old_batch) == self.batch_size
        return bytes(0)
