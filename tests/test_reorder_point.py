import unittest
from src.reorder_point import calculate_reorder_point

class TestReorderPoint(unittest.TestCase):

    def test_reorder_point(self):
        lead_times = 10
        products_sold = 200
        stock_levels = 50
        lead_time_std = 5
        demand_std = 20
        result = calculate_reorder_point(lead_times, products_sold, stock_levels, lead_time_std, demand_std)
        self.assertAlmostEqual(result, 73.178, places=2)

if __name__ == '__main__':
    unittest.main()
