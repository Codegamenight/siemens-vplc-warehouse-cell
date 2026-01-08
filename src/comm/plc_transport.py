class PLCConfig:
    def __init__(self, mode="MOCK"):
        self.mode = mode

class MockTransport:
    def __init__(self, cfg: PLCConfig):
        self.db = bytearray(64)

    def read_db(self) -> bytearray:
        return self.db

    def write_db(self, data: bytes):
        self.db = bytearray(data)
