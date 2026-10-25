# test_nfttorrent.py
"""
Tests for NftTorrent module.
"""

import unittest
from nfttorrent import NftTorrent

class TestNftTorrent(unittest.TestCase):
    """Test cases for NftTorrent class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = NftTorrent()
        self.assertIsInstance(instance, NftTorrent)

    def test_run_method(self):
        """Test the run method."""
        instance = NftTorrent()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
