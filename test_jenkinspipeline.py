# test_jenkinspipeline.py
"""
Tests for JenkinsPipeline module.
"""

import unittest
from jenkinspipeline import JenkinsPipeline

class TestJenkinsPipeline(unittest.TestCase):
    """Test cases for JenkinsPipeline class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = JenkinsPipeline()
        self.assertIsInstance(instance, JenkinsPipeline)
        
    def test_run_method(self):
        """Test the run method."""
        instance = JenkinsPipeline()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
