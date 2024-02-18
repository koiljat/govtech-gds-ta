import unittest
import pandas as pd
from task1.task1a import map_replace


class TestDataReader(unittest.TestCase):
    def test_validate_results(self):
        """Check there are end results."""
        restaurants = pd.read_csv("results/restaurants.csv")
        restaurant_events = pd.read_csv("results/restaurant_events.csv")
        self.assertIsNotNone(restaurants)
        self.assertIsNotNone(restaurant_events)
        self.assertTrue(len(restaurants) > 0)
        self.assertTrue(len(restaurant_events) > 0)

    def test_duplicates(self):
        """Check for duplicates in the data."""
        restaurants = pd.read_csv("results/restaurants.csv")
        restaurant_events = pd.read_csv("results/restaurant_events.csv")
        duplicate_restaurants = restaurants[restaurants.duplicated()]
        duplicate_events = restaurant_events[restaurant_events.duplicated()]
        self.assertEqual(len(duplicate_restaurants), 0)
        self.assertEqual(len(duplicate_events), 0)

    def test_missing_values(self):
        """Check for missing values in the data."""
        restaurants = pd.read_csv("results/restaurants.csv")
        restaurant_events = pd.read_csv("results/restaurant_events.csv")
        self.assertFalse(restaurants.isnull().values.any())
        self.assertFalse(restaurant_events.isnull().values.any())
    
        
if __name__ == '__main__':
    unittest.main()
