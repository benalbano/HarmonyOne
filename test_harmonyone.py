# test_harmonyone.py
"""
Tests for HarmonyOne module.
"""

import unittest
from harmonyone import HarmonyOne

class TestHarmonyOne(unittest.TestCase):
    """Test cases for HarmonyOne class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HarmonyOne()
        self.assertIsInstance(instance, HarmonyOne)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HarmonyOne()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
