import unittest
from src.safety_stock import calculate_safety_stock

class TestSafetyStock(unittest.TestCase):

    def test_safety_stock(self):
        lead_time_std = 5
        demand_std = 20
        result = calculate_safety_stock(lead_time_std, demand_std)
        self.assertAlmostEqual(result, 33.178, places=2)

if __name__ == '__main__':
    unittest.main()
