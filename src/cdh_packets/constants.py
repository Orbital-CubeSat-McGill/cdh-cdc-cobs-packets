"""Wire-protocol constants shared by BBG, RB, and ground.

Must match MPM-Ion0-software/docs/greenbear-protocol.md.
"""

from __future__ import annotations

CALLSIGN: bytes = b"VE3 JKB"  # exactly 7 ASCII bytes; sync word + legal ID
VERSION: int = 1
HEADER_SIZE: int = 16  # callsign(7) + version(1) + seq(2) + time(4) + length(2)
CRC_SIZE: int = 2
MAX_CONTENT: int = 1024  # launch ceiling; absolute air ceiling is 2025

# CRC-16/CCITT-FALSE
CRC_POLY: int = 0x1021
CRC_INIT: int = 0xFFFF
CRC_CHECK: int = 0x29B1  # binascii.crc_hqx(b"123456789", 0xFFFF)
