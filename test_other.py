"""
tests for other.py
"""

import other


class TestOther:

    def test_add_suffix(self):
        assert "Tosia bolek" == other.add_suffix("bolek")
