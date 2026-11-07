"""Green Bear USB framing: COBS + logical packet (header + CRC-16).

Fill ``cobs.encode`` / ``cobs.decode`` and ``packet.build`` / ``packet.parse``.
The test suites in MPM-Ion0-software (``Ion/tests/test_cobs.py``,
``Ion/tests/test_packet.py``) are the spec — this package stays light.
"""

from __future__ import annotations

from cdh_packets import cobs, constants, packet
from cdh_packets.packet import Packet

__all__ = [
    "Packet",
    "cobs",
    "constants",
    "packet",
]
