import unittest
import pandas as pd

class MyTestCase(unittest.TestCase):
    def test_missing_values(self):
        df = pd.DataFrame({'A': [1, 2, None, 4, 5], 'B': [None, 2, 3, 4, 5]})
        
        # Assert that there are missing values in the DataFrame
        self.assertTrue(df.isnull().values.any(), "Missing values found in the DataFrame")
    
    def test_duplicate_values(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 2, 3, 4, 5]})
        
        # Assert that there are duplicate values in the DataFrame
        self.assertTrue(df.duplicated().any(), "Duplicate values found in the DataFrame")


if __name__ == '__main__':
    unittest.main()