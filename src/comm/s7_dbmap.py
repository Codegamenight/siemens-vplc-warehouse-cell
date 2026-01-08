def get_bool(db: bytearray, byte: int, bit: int) -> bool:
    return (db[byte] >> bit) & 1 == 1

def set_bool(db: bytearray, byte: int, bit: int, val: bool):
    if val:
        db[byte] |= 1 << bit
    else:
        db[byte] &= ~(1 << bit)

def set_uint16(db: bytearray, offset: int, val: int):
    db[offset] = (val >> 8) & 0xFF
    db[offset+1] = val & 0xFF
