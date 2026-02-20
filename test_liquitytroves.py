# test_liquitytroves.py
"""
Tests for LiquityTroves module.
"""

import unittest
from liquitytroves import LiquityTroves

class TestLiquityTroves(unittest.TestCase):
    """Test cases for LiquityTroves class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LiquityTroves()
        self.assertIsInstance(instance, LiquityTroves)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LiquityTroves()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
